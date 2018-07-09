import descarteslabs as dl
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# define the region of interest
shp = dl.places.shape('europe_italy_firenze')

# query for available scenes for all of 2017
fc = dl.metadata.search(geom=shp['geometry'], products='sentinel-2:L1C',
                        start_time='2017-01-04', end_time='2017-12-31', limit=1000)

# keep the scenes with less than 5% cloud cover; cloud_fraction_0 is the cloud fraction of the scene as calculated by Descartes
# using the cloud mask supplied by the imagery provider (in this case ESA)
cloud_threshold = 0.05
ids = [feat['properties']['key'] for feat in fc['features'] if feat['properties']['cloud_fraction_0'] < cloud_threshold]

# define the data and physical ranges for NDVI for Sentinel-2
band_information = dl.metadata.get_bands_by_constellation('S2A')
data_range = band_information['ndvi']['data_range']
physical_range = band_information['ndvi']['physical_range']

# build an ndvi time stack; using 100m resolution here just for demonstration purposes
ndvi_stack = []
for scene_id in ids:
    img, meta = dl.raster.ndarray([scene_id], 
                                    bands=['ndvi', 'alpha'], 
                                    scales=[[data_range[0], data_range[1], physical_range[0], physical_range[1]]], 
                                    data_type='Float32', 
                                    resolution=100, 
                                    cutline=shp['geometry'])
    
    ndvi = img[:, :, 0]
    # alpha channel indicates data or no data 
    alpha = img[:, :, 1]
    # mask out no data
    nodata = alpha == 0
    masked = np.where(nodata, 0, ndvi)
    # add masked ndvi array to stack
    ndvi_stack.append(masked)

# make numpy array; shape is (ndates, ypixels, xpixels)
ndvi_stack = np.asarray(ndvi_stack)

# calculate statistics over time dimension
max_ndvi = np.ma.masked_equal(ndvi_stack, 0).max(axis=0)
min_ndvi = np.ma.masked_equal(ndvi_stack, 0).min(axis=0)
mean_ndvi = np.ma.masked_equal(ndvi_stack, 0).mean(axis=0)
std_ndvi = np.ma.masked_equal(ndvi_stack, 0).std(axis=0)

# use all the observations where we have data as features
# shape is (nsamples, nfeatures)
features = np.dstack([max_ndvi[max_ndvi.mask==True], min_ndvi[min_ndvi.mask==True], mean_ndvi[mean_ndvi.mask==True], std_ndvi[std_ndvi.mask==True]]).squeeze()

# randomly assign classes to each of the samples (pixels) and use as truth (here you will determine your own tags)
nclasses = 2
truth = np.random.randint(0, nclasses, features.shape[0])

# randomly shuffle the data
perm = np.random.permutation(truth.shape[0])
features = features[perm, :]
truth = truth[perm]

# 80/20 split for training/testing
split = int(truth.shape[0] * 0.8)
train_X = features[:split, :]
train_Y = truth[:split]
test_X = features[split:, :]
test_Y = truth[split:]

# randomly shuffle the training data again
perm = np.random.permutation(train_Y.shape[0])
train_X = train_X[perm, :]
train_Y = train_Y[perm]

# train a classifier
model = RandomForestClassifier()
model.fit(train_X, train_Y)

# test the classifier
pred = model.predict(test_X)
# accuracy, precision, recall; more available here http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
accuracy = accuracy_score(test_Y, pred)
precision = precision_score(test_Y, pred)
recall = recall_score(test_Y, pred)
