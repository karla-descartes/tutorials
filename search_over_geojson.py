import descarteslabs as dl
import descarteslabs.common.scenes as scn

# The bounding box geometry of Haiti  
haiti = {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -74.520263671875,
              17.98918266463051
            ],
            [
              -71.685791015625,
              17.98918266463051
            ],
            [
              -71.685791015625,
              19.94236918954201
            ],
            [
              -74.520263671875,
              19.94236918954201
            ],
            [
              -74.520263671875,
              17.98918266463051
            ]
          ]
        ]
      }
    }


# Create a SceneCollection  
scenes = scn.search(haiti['geometry'],
                    products=["sentinel-2:L1C"],
                    start_datetime="2018-05-01",
                    end_datetime="2018-05-15",
                    cloud_fraction=0.7)

print("There are {} scenes in the collection".format(len(scenes)))


# # View the GeospatialContext of the SceneCollection. The GeospatialContext is what ensures the spatial resolution,
# # geometry, and coordinate system of returned data are comparable, even if their native properties differ.
# print(scenes.ctx)

# # Get unique information about the number of scenes by product
# for product in scenes.groupby("properties.product"):
#     print(product)

# # You can modify attributes of the GeospatialContext
# ctx = scenes.ctx
# ctx_lowres = ctx.assign(resolution=120)

# # Request a NumPy stack of all the scenes in the same GeospatialContext
# arr_stack = scenes.stack("red green blue", ctx=ctx_lowres)
