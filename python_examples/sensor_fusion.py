import descarteslabs as dl

# Define a bounding box around Taos in a GeoJSON
taos = {
      "type": "Feature",
      "properties": {},
      "geometry": {
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
    }


# Create a SceneCollection  
scenes, ctx = dl.scenes.search(taos['geometry'],
                    products=["landsat:LC08:01:RT:TOAR", "sentinel-2:L1C"],
                    start_datetime="2018-05-01",
                    end_datetime="2018-05-15",
                    cloud_fraction=0.7,
                    limit=15
                   )
print("There are {} scenes in the collection, both Sentinel 2 and Landsat 8.".format(len(scenes)))


# View the GeospatialContext of the SceneCollection. The GeospatialContext is what ensures the spatial resolution,
# geometry, and coordinate system of returned data are comparable, even if their native properties differ.
print(ctx)

# Get unique information about the number of scenes by product
for product in scenes.groupby("properties.product"):
    print(product)

# You can modify attributes of the GeospatialContext
ctx_lowres = ctx.assign(resolution=120)

# Request a NumPy stack of all the scenes in the same GeospatialContext
arr_stack = scenes.mosaic("red green blue", ctx=ctx_lowres)

# dl.scenes.display(arr_stack, size=16)