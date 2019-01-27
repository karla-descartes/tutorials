import descarteslabs as dl 

osm = dl.vectors.FeatureCollection("f69f372b369649f2927f40445928144")

places = dl.Places()
results = places.search('nairobi')


slug = results[0]['slug']
place = places.shape(slug)
shape = place['geometry']

fc = osm.filter(geometry=shape)
print(list(fc.features()))
