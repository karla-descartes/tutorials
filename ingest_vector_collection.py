import descarteslabs as dl 
# import shapely.geometry 
import json

# fcs = dl.vectors.FeatureCollection.list()


marine_protected_areas = dl.vectors.FeatureCollection.create(
	name="brazil_2",
	title="Marine Protected Areas",
	description="Protected areas coverage in 2018")




# geojson = json.load(open('/Users/karlaking/Downloads/WDPA_Oct2018_marine-shapefile/WDPA.geojson'))
geojson = json.load(open('/Users/karlaking/descartes-code/client-code/crop-yield/data/Brazil.geojson'))

areas = [dl.vectors.Feature(feat['geometry'], feat['properties']) for feat in geojson['features']]
# I can confirm the resulting list objects are of type class 'descarteslabs.vectors.feature.Feature'>

marine_protected_areas.add(areas)