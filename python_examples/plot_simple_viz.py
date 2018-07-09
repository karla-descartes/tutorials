"""
==================================================
Simple Image Visualization
==================================================

Visualize a true color Landsat 8 SceneCollection.

"""

import descarteslabs as dl

# Create a tile around Paris, France
tile = dl.scenes.DLTile.from_latlon(43.7230,
                                    10.3966,
                                    resolution=20.0,
                                    tilesize=5024,
                                    pad=0)

# Use the Scenes API to search for imagery availble over the area of interest
scenes, ctx = dl.scenes.search(tile,
                               products=["landsat:LC08:01:RT:TOAR"],
                               start_datetime="2018-01-01",
                               end_datetime="2018-06-01",
                               limit=2,
                               cloud_fraction=.1)


print(scenes)

# Mosaic the scenes data
arr = scenes.mosaic("red green blue", ctx)


# Display the mosaic
# dl.scenes.display(arr[0][0], size=16)
# dl.scenes.display(arr[0][1], size=16)
# dl.scenes.display(arr[0][2], size=16)
