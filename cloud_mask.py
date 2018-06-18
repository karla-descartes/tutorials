import descarteslabs as dl 

tile = dl.raster.dltile_from_latlon(1.33883688455388, 
                                    103.8369369506836, 
                                    resolution = 20.0,
                                    tilesize = 1024,
                                    pad = 0)


scenes = dl.metadata.search(
					   products=["sentinel-2:L1C"],
                       start_time='2018-01-01',
                       end_time='2018-03-30',
                       geom=tile['geometry'],
                       limit = 10,
                       cloud_fraction=.2
                       )

ids = [img['id'] for img in scenes['features']]

arr, meta = dl.raster.ndarray(ids,		
						bands=['red', 'green', 'blue', 'cloud-mask'],
						scales=[[0,4000], [0, 4000], [0, 4000], None],
						cutline=tile['geometry'])


cloud_mask = arr[:, :, 3]
arr[cloud_mask == 1] = 0

 


