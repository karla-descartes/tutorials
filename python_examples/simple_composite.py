import descarteslabs as dl

# Create a tile around Paris, France
tile = dl.raster.dltile_from_latlon(43.7230,  
                                    10.3966, 
                                    resolution = 20.0,
                                    tilesize = 1024,
                                    pad = 0)

# Use the Scenes API to search for imagery availble over the area of interest
scenes, ctx = dl.scenes.search(tile['geometry'],
	                products=["landsat:LC08:01:RT:TOAR"],
                    start_datetime="2018-01-01",
                    end_datetime="2018-06-01",
                    limit=2,
                    cloud_fraction=.1
                   )


# Mosaic the scenes data
arr = scenes.mosaic("red green blue", ctx)

# Display the mosaic
dl.scenes.display(arr, size=16)