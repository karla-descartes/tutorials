import descarteslabs as dl
import descarteslabs.common.scenes as scn

# Get the geometry of Taos from the Places API
matches = dl.places.find('new-mexico_taos')
aoi = matches[0]
shape = dl.places.shape(aoi['slug'], geom='low')


# Create a SceneCollection  
scenes = scn.search(shape['geometry'],
                    products=["landsat:LC08:01:RT:TOAR", "sentinel-2:L1C"],
                    start_datetime="2018-05-01",
                    end_datetime="2018-05-15",
                    cloud_fraction=0.7,
                    limit=15
                   )
print("There are {} scenes in the collection, both Sentinel 2 and Landsat 8.".format(len(scenes)))


# View the GeospatialContext of the SceneCollection. The GeospatialContext is what ensures the spatial resolution,
# geometry, and coordinate system of returned data are comparable, even if their native properties differ.
print(scenes.ctx)

# Get unique information about the number of scenes by product
for product in scenes.groupby("properties.product"):
    print(product)

# You can modify attributes of the GeospatialContext
ctx = scenes.ctx
ctx_lowres = ctx.assign(resolution=120)

# Request a NumPy stack of all the scenes in the same GeospatialContext
arr_stack = scenes.stack("red green blue", ctx=ctx_lowres)
