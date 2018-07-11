from descarteslabs.ext.catalog import catalog
import descarteslabs as dl 


product = catalog.add_product(
	"simple_image_51",
	title="Simple Product Creation",
	description="Blargh",
	)

product_id = product['data']['id']



bands = ['red', 'green', 'blue']
i = 0

# Get info from catalog or from file 
for band in bands:
	i +=1
	catalog.add_band(product_id,
		band,
		jpx_layer=0,
		srcfile=0,
		srcband=i,
		nbits=14,
		dtype='UInt16',
		nodata=0,
		data_range=[0,10000],
		type='spectral',
		default_range=(0,4000)
		)



geometry = {"type":"Polygon","coordinates":[[[2.165946315534452,48.713171120067045],[2.5359015712706023,48.713171120067045],[2.5359015712706023,48.957687975409726],[2.165946315534452,48.957687975409726],[2.165946315534452,48.713171120067045]]]}


scenes_meta = dl.metadata.search(product='sentinel-2:L1C',
                              start_time='2018-06-24',
                              end_time='2018-06-30',
                              geom=geometry,
                              limit=2,
                              cloud_fraction=.1)

image_ids = [img['id'] for img in scenes_meta['features']]



img_data, meta = dl.raster.ndarray(
	image_ids,
	bands=['red', 'green', 'blue'],
	resolution=20,
	cutline=geometry
)

catalog.upload_ndarray(
	img_data,
	product_id=product_id,
	image_id="Paris",
	raster_meta=meta)




