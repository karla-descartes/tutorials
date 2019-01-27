import descarteslabs as dl

gdelt = list(filter(lambda fc: 'gdelt' in fc.name, dl.vectors.FeatureCollection.list()))
print("Available GDELT tables:")
print(gdelt)


fc = dl.vectors.FeatureCollection(gdelt[0].id) 


places = dl.Places()
results = places.search('nairobi')


slug = results[0]['slug']

place = places.shape(slug)

shape = place['geometry']

fc = fc.filter(geometry=shape)
print(list(fc.features()))