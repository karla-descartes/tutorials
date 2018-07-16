import descarteslabs as dl


# Define a bounding box around Taos in a GeoJSON
taos = {"type": "Polygon",
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
scenes, ctx = dl.scenes.search(taos['geometry'],
                    products="landsat:LC08:01:RT:TOAR",
                    start_datetime="2018-01-01",
                    end_datetime="2018-12-31",
                    cloud_fraction=0.7,
                    limit=500
                   )
print("There are {} scenes in the collection.".format(len(scenes)))


# To create subcollections using the Scenes API, we have the built in methods 'each', 'grouby', and 'filter' 
# These methods empower you to further isolate timestacks of interest when perform analysis


# To access every scenes' month, you can call the each method using dot notation to expose the properties of all instances
scenes.each.properties.date.month


# Similarly, if we want to create multiple subsets based on those properties, we can use the 'groupby' method
for (year, month), month_scenes in scenes.groupby("properties.date.year", "properties.date.month"):
    print("{} {}: {} scenes".format(year, month, len(month_scenes)))


# You can further group the subsets using the built in 'method' filter 
spring_scenes = scenes.filter(lambda s: s.properties.date.month > 2 and s.properties.date.month < 6)
fall_scenes = scenes.filter(lambda s: s.properties.date.month > 8 and s.properties.date.month < 12)

print("There are {} Spring scenes & {} Fall scenes.".format(len(spring_scenes), len(fall_scenes)))

