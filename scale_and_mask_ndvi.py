import descarteslabs as dl
import numpy as np


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
  end_time="2018-05-15", limit=2)

# Fetch the band information using the Metadata API, including the NDVI ranges 
band_info = dl.metadata.bands("modis:09:CREFL")
physical_range = []
valid_range = [] 

for band in band_info:
  if band["name"] == "ndvi":
    physical_range = band["physical_range"]
    valid_range = band["data_range"]



# Isolate the image IDs to pull data for 
feat_ids = [feat['id'] for feat in fc['features']]


# Request the NDVI band and scale it accordingly and the alpha band for masking next 
arr, meta = dl.raster.ndarray(
        feat_ids,
        cutline=nigeria['geometry'],
        bands=['ndvi', 'alpha'],
        scales=[[valid_range[0], valid_range[1], physical_range[0], physical_range[1]], None],
        data_type='Float32'
        )

        
# mask out nodata pixels
nodata = arr[:,:,-1] == 0
masked = np.where(nodata, 0, arr[:,:,0])
print np.unique(masked, return_counts=True)











           