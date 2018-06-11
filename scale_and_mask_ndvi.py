import descarteslabs as dl


# The bounding box geometry of Nigeria  
nigeria = {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
             [
              2.5048828125,
              4.039617826768437
            ],
            [
              14.589843749999998,
              4.039617826768437
            ],
            [
              14.589843749999998,
              13.966054081318314
            ],
            [
              2.5048828125,
              13.966054081318314
            ],
            [
              2.5048828125,
              4.039617826768437
            ]
          ]
        ]
      }
    }


# Request Modis imagery, which contains indicies that need to be scaled 
fc = dl.metadata.search(products="modis:09:CREFL", geom=nigeria['geometry'], start_time="2017-05-01", 
  end_time="2018-05-15", limit=1)

# Valid and physical ranges of band values can be found in the Catalog band metadata
valid_range = [0,16000]
physical_range = [-0.6, 1.0]

# Isolate the image IDs to pull data for 
feat_ids = [feat['id'] for feat in fc['features']]
print len(feat_ids)

# Request the NDVI band and scale it accordingly and the alpha band for masking next 
data, meta = dl.raster.ndarray(feat_ids, 
                bands=['ndvi', 'alpha'], 
                scales=[[valid_range[0], valid_range[1], physical_range[0], physical_range[1]], None],
                cutline=nigeria['geometry'], data_type='Float32',)

# Import NumPy to map nodata values to 2, outside the data's valid range 
import numpy as np
        
nodata = data[:,:,1] == 0
masked = np.where(nodata, 2, data[:,:,0])
print (np.unique(masked, return_counts=True))









           