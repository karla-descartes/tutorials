
Land Cover Classification
=========================

Objective: Classify an image using the Scenes API and SciKit Learn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This image classification uses the Scenes API to filter the Landsat 8
Real Time Collection for relatively cloud free imagery above a small
area in New Zealand. The tutorial uses GDAL to rasterize training data
and scikit-learn to train and run a Random Forest Classification. We
begin by importing the necessary libraries.

.. code:: ipython3

    import descarteslabs as dl
    from osgeo import gdal
    import os
    import numpy as np
    from sklearn import metrics
    from sklearn.ensemble import RandomForestClassifier 
    import matplotlib.pyplot as plt
    %matplotlib inline

Lake Taupo is located on the North Island of New Zealand. The GeoJSON
feature defined below is a rectangle containing the lake, mountains, and
plantations. This feature will be used to search for imagery and as the
extent of our analysis.

.. code:: ipython3

    lake_taupo = {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              175.55877685546875,
              -39.27691581029594
            ],
            [
              176.319580078125,
              -39.27691581029594
            ],
            [
              176.319580078125,
              -38.638327308061875
            ],
            [
              175.55877685546875,
              -38.638327308061875
            ],
            [
              175.55877685546875,
              -39.27691581029594
            ]
          ]
        ]
      }
    }

Get data from Scenes API
------------------------

The Scenes API allows you to query our catalog of imagery. Here, we
specify the geometry, product, and cloud fraction parameters to reflect
our study's requirements. The ``search`` method returns a tuple
containing the Scene Collection, and the GeospatialContext, where the
first lists the image IDs and other metadata. The latter defines the
spatial resolution, coordinate system, and other spatial parameters to
apply to the Scenes.

.. code:: ipython3

    scenes, ctx = dl.scenes.search(lake_taupo['geometry'],
                        products=["landsat:LC08:01:RT:TOAR"],
                        start_datetime="2017-12-11",
                        end_datetime="2017-12-12",
                        cloud_fraction=0.7
                       )
    ctx




.. parsed-literal::

    AOI(geometry=<shapely.geom... 0x1a17bc8828>,
        resolution=15,
        crs='EPSG:32660',
        align_pixels=True,
        bounds=(175.55877685546875, -39.27691581029594, 176.319580078125, -38.638327308061875),
        shape=None)



.. code:: ipython3

    # You can modify the GeospatialContext as needed.
    lowres_context = ctx.assign(resolution=60,crs='EPSG:32760')

.. code:: ipython3

    arr = scenes[0].ndarray("red green blue",lowres_context)

A call to ``ndarray`` on one Scene from the Scene collection returns a
masked array with the image's data.

.. code:: ipython3

    # Set raster metadata for rasterizing our training data.
    bands, rows, cols = arr.shape
    geo_transform = [374566.1760405825, 60.0, 0.0, -4276862.181956149, 0.0, -60.0]
    proj = 'PROJCS["WGS 84 / UTM zone 60N", GEOGCS["WGS 84", DATUM["WGS_1984", SPHEROID["WGS 84",6378137,298.257223563, AUTHORITY["EPSG","7030"]], AUTHORITY["EPSG","6326"]], PRIMEM["Greenwich",0, AUTHORITY["EPSG","8901"]], UNIT["degree",0.0174532925199433, AUTHORITY["EPSG","9122"]], AUTHORITY["EPSG","4326"]], PROJECTION["Transverse_Mercator"], PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",177],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],PARAMETER["false_northing",0], UNIT["metre",1, AUTHORITY["EPSG","9001"]], AXIS["Easting",EAST], AXIS["Northing",NORTH], AUTHORITY["EPSG","32660"]]'

.. code:: ipython3

    # Stack the bands of the data to prepare for classification
    stacked = np.dstack((arr[0],arr[1],arr[2]))

.. code:: ipython3

    # Display the image data
    dl.scenes.display(arr, size=12)



.. image:: https://cdn.descarteslabs.com/descarteslabs-python/land_cover/output_12_0.png


Write helper functions to rasterize vector
------------------------------------------

We need a library of functions to rasterize our training data.

.. code:: ipython3

    def create_mask_from_vector(vector_data_path, cols, rows, geo_transform,
                                projection, target_value=1):
        """Rasterize the given vector (wrapper for gdal.RasterizeLayer)."""
        data_source = gdal.OpenEx(vector_data_path, gdal.OF_VECTOR)
        layer = data_source.GetLayer(0)
        driver = gdal.GetDriverByName('MEM')  # In memory dataset
        target_ds = driver.Create('', cols, rows, 1, gdal.GDT_UInt16)
        target_ds.SetGeoTransform(geo_transform)
        target_ds.SetProjection(projection)
        gdal.RasterizeLayer(target_ds, [1], layer, burn_values=[target_value])
        return target_ds
    
    
    def vectors_to_raster(file_paths, rows, cols, geo_transform, projection):
        """Rasterize the vectors in the given directory in a single image."""
        labeled_pixels = np.zeros((rows, cols))
        print
        for i, path in enumerate(file_paths):
            label = i+1
            ds = create_mask_from_vector(path, cols, rows, geo_transform,
                                         projection, target_value=label)
            band = ds.GetRasterBand(1)
            labeled_pixels += band.ReadAsArray()
            ds = None
        return labeled_pixels
    
    
    def write_geotiff(fname, data, geo_transform, projection):
        """Create a GeoTIFF file with the given data."""
        driver = gdal.GetDriverByName('GTiff')
        rows, cols = data.shape
        dataset = driver.Create(fname, cols, rows, 1, gdal.GDT_Byte)
        dataset.SetGeoTransform(geo_transform)
        dataset.SetProjection(projection)
        band = dataset.GetRasterBand(1)
        band.WriteArray(data)
        dataset = None  # Close the file

Load training data
------------------

The data used to train the classifier are individual shapefiles being
read in from file.

.. code:: ipython3

    train_data_path = "data/train/"
    validation_data_path = "data/test/"

.. code:: ipython3

    files = [f for f in os.listdir(train_data_path) if f.endswith('.shp')]
    classes = [f.split('.')[0] for f in files]
    print("There are {} classes:".format(len(classes)))
    for c in classes:
        print(c)
     
    shapefiles = [os.path.join(train_data_path, f)
                  for f in files if f.endswith('.shp')]
    
    labeled_pixels = vectors_to_raster(shapefiles, rows, cols, geo_transform,
                                       proj)
    is_train = np.nonzero(labeled_pixels)
    training_labels = labeled_pixels[is_train]
    training_samples = stacked[is_train]


.. parsed-literal::

    There are 5 classes:
    clear_cut
    urban
    mature_plantation
    other
    water


Train the classifier and run the land cover classification
----------------------------------------------------------

.. code:: ipython3

    classifier = RandomForestClassifier(n_jobs=-1)
    classifier.fit(training_samples, training_labels)




.. parsed-literal::

    RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                max_depth=None, max_features='auto', max_leaf_nodes=None,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=-1,
                oob_score=False, random_state=None, verbose=0,
                warm_start=False)



.. code:: ipython3

    n_samples = rows*cols
    flat_pixels = stacked.reshape((n_samples, bands))
    result = classifier.predict(flat_pixels)
    classification = result.reshape((rows, cols))

.. code:: ipython3

    plt.figure(figsize=[7,7])
    plt.imshow(classification)
    plt.title('Classified Landcover')
    dl.scenes.display(arr, size=6.1, title="Original Image")



.. image:: https://cdn.descarteslabs.com/descarteslabs-python/land_cover/output_21_0.png



.. image:: https://cdn.descarteslabs.com/descarteslabs-python/land_cover/output_21_1.png


Accuracy assessment
-------------------

.. code:: ipython3

    shapefiles = [os.path.join(validation_data_path, "%s.shp"%c) for c in classes]
    verification_pixels = vectors_to_raster(shapefiles, rows, cols, geo_transform, proj)
    for_verification = np.nonzero(verification_pixels)
    verification_labels = verification_pixels[for_verification]
    predicted_labels = classification[for_verification]

.. code:: ipython3

    print("Confussion matrix:\n\n{}".format(metrics.confusion_matrix(verification_labels, predicted_labels)))


.. parsed-literal::

    Confussion matrix:
    
    [[12  0  3  0  0]
     [ 0  3  0  0  0]
     [ 2  0 16  1  0]
     [ 2  0  1  9  0]
     [ 0  0  0  0 19]]


.. code:: ipython3

    target_names = ['Class {}'.format(s) for s in classes]
    print("Classification report:\n\n {}".format(metrics.classification_report(verification_labels, predicted_labels,
                                        target_names=target_names)))
    print("Classification accuracy: {}".format(metrics.accuracy_score(verification_labels, predicted_labels)))


.. parsed-literal::

    Classification report:
    
                              precision    recall  f1-score   support
    
            Class clear_cut       0.75      0.80      0.77        15
                Class urban       1.00      1.00      1.00         3
    Class mature_plantation       0.80      0.84      0.82        19
                Class other       0.90      0.75      0.82        12
                Class water       1.00      1.00      1.00        19
    
                avg / total       0.87      0.87      0.87        68
    
    Classification accuracy: 0.8676470588235294

.. only:: builder_html

   Download :download:`the example training data <data_files/train.zip>` and :download:`example test data <data_files/test.zip>`

