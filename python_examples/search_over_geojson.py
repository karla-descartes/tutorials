import descarteslabs as dl

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
scenes, ctx = dl.scenes.search(haiti['geometry'],
                    products=["sentinel-2:L1C"],
                    start_datetime="2018-05-01",
                    end_datetime="2018-05-03",
                    cloud_fraction=0.7,
                    limit=5)

print("There are {} scenes in the collection".format(len(scenes)))

# Mosaic returned scenes and display
mosaic = scenes.mosaic(bands = "red green blue", ctx= ctx)

dl.scenes.display(mosaic, title="Haiti Mosaic")