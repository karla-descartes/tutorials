import numpy as np
import collections
import descarteslabs as dl
import descarteslabs.common.scenes as scn



# Get the geometry of Taos from 
matches = dl.places.find('new-mexico_taos')
aoi = matches[0]
shape = dl.places.shape(aoi['slug'], geom='low')

# Create a SceneCollection  
scenes = scn.search(shape['geometry'],
                    products="landsat:LC08:01:RT:TOAR",
                    start_datetime="2017-01-01",
                    end_datetime="2017-12-31",
                    cloud_fraction=0.7,
                    limit=500
                   )
print("There are {} scenes in the collection.".format(len(scenes)))
# There are 53 scenes in the collection.


# To create subcollections using the Scenes API, we have the built in methods 'each', 'grouby', and 'filter' 
# These methods empower you to further isolate timestacks of interest when perform analysis


# To access every scenes' month, you can call the each method using dot notation to expose the properties of all instances
scenes.each.properties.date.month


# Similarly, if we want to create multple subsets based on those properties, we can use the groupby method
for (year, month), month_scenes in scenes.groupby("properties.date.year", "properties.date.month"):
    print("{} {}: {} scenes".format(year, month, len(month_scenes)))

# 2017 5: 6 scenes
# 2017 6: 4 scenes
# 2017 7: 8 scenes
# 2017 8: 5 scenes
# 2017 9: 8 scenes
# 2017 10: 8 scenes
# 2017 11: 6 scenes
# 2017 12: 8 scenes

# Finally, if you are interseted in returning a unique subset of the SceneCollection, use the filter method along with a lambda to further query the return
fall_scenes = scenes.filter(lambda s: s.properties.date.month > 8 and s.properties.date.month < 12)
sprint_scenes = scenes.filter(lambda s: s.properties.date.month > 2 and s.properties.date.month < 6)

print("There are {} Fall scenes & {} Spring scenes.".format(len(fall_scenes), len(sprint_scenes)))