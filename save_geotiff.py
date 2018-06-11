import descarteslabs as dl

# Create a geojson feature to clip imagery to
box = {"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[-108.64292971398066,33.58051349561343],[-108.27082685426221,33.58051349561343],[-108.27082685426221,33.83925599538719],[-108.64292971398066,33.83925599538719],[-108.64292971398066,33.58051349561343]]]},"properties":'null'}]}

# Two predefined image IDs for mosaic and download. These can be obtained through a Metadata or Scenes API search
images = ['landsat:LC08:01:RT:TOAR:meta_LC08_L1TP_035037_20180602_20180602_01_RT_v1','landsat:LC08:01:RT:TOAR:meta_LC08_L1TP_035036_20180602_20180602_01_RT_v1']

# The Raster API call to download an image mosaic. Other parameters are available
dl.raster.raster(
	inputs=images,
	bands=['red', 'green', 'blue', 'swir2'],
	scales=[[0,5500], [0, 5500], [0, 5500], [0, 5500]],
	data_type='Byte',
	cutline=box['features'][0]['geometry'],
	save=True,
	outfile_basename='save_local'
	)


