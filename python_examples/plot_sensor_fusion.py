"""
==================================================
Mosaic Multi-Product Imagery
==================================================

Composite imagery from two data sources and
display as a single image.

"""

import descarteslabs as dl
import numpy as np

# Define a bounding box around Taos in a GeoJSON

taos = {
    "type": "Polygon",
    "coordinates": [
        [
            [
                -105.71868896484375,
                36.33725319397006
            ],
            [
                -105.2105712890625,
                36.33725319397006
            ],
            [
                -105.2105712890625,
                36.73668306473141
            ],
            [
                -105.71868896484375,
                36.73668306473141
            ],
            [
                -105.71868896484375,
                36.33725319397006
            ]
        ]
    ]
}

# Create a SceneCollection
scenes, ctx = dl.scenes.search(taos,
                               products=["landsat:LC08:01:RT:TOAR", "sentinel-2:L1C"],
                               start_datetime="2018-05-01",
                               end_datetime="2018-05-15",
                               cloud_fraction=0.1,
                               limit=15)

print(scenes)

# View the GeospatialContext of the SceneCollection. The GeospatialContext is what ensures the spatial resolution,
# geometry, and coordinate system of returned data are comparable, even if their native properties differ.
print(ctx)

# Get unique information about the number of scenes by product
for product in scenes.groupby("properties.product"):
    print(product)

# You can modify attributes of the GeospatialContext
ctx_lowres = ctx.assign(resolution=60)

# Request a NumPy stack of all the scenes in the same GeospatialContext
arr_stack = scenes.stack("red green blue", ctx=ctx_lowres)


composite = np.ma.median(arr_stack, axis=0)
dl.scenes.display(composite, title="Taos Composite")

