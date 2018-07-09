============
Descartes Labs Web Interfaces 
============

The Descartes Labs programmatic APIs have accompanying web interfaces to create a more user friendly experience. Some of those web interfaces are described below. 

***************
 Viewer 
***************
The `Descartes Labs Viewer <https://viewer.descarteslabs.com>`_ sits on top of our Metadata API and provides full visual display and filtering access of available imagery. By default, the Landsat 8 Real Time product is loaded centered on your location (if available). You can choose to add new layers, or remove, toggle, and edit currently loaded layers. The edit option allows you to query the dataset by date and cloud fraction as well as visualize different band combinations. 

**Generate a Static XYZ Layer** 

XYZ is a `tiling protocol <https://en.wikipedia.org/wiki/Tiled_web_map>`_  that can be used by a mapping client like ArcGIS or QGIS to access image data. `Viewer <https://viewer.descarteslabs.com>`_ allows users to generate a static XYZ URL of imagery that can be imported into other mapping environments. To generate an XYZ URL, you click the ellipsis next to the layer of interest, and select "Create static XYZ". The URL will appear in the drop-down menu of your saved Static XYZ URLs. Once you have a static XYZ URL, you can add it to any number of map applications that support XYZ protocol.  Here is more information about how to use a static layer in `QGIS <https://www.spatialbias.com/2018/02/qgis-3.0-xyz-tile-layers/>`_ and `ArcGIS <https://gis.stackexchange.com/questions/174569/adding-custom-web-tile-layer-to-arcmap>`_.

******************
 GeoVisual Search   
******************

GeoVisual Search (GVS) is the our computer vision product used to detect features on the earth surface based on a sample. Our `Search interface <http://search.descarteslabs.com/>`_ is powered by the same intelligent object detection technology, enabling a user to place a bounding box around a feature anywhere in the US (covered with high resolution imagery). It returns a subset of the top visual matches. One potential search feature would be a substation, returning a collection of substations across the US. 

***************
 Catalog 
***************

The Descartes Labs `Catalog <https://catalog.descarteslabs.com/?/>`_  is a list of all image products and their associated metadata. This includes, but is not limited to, things like the valid time range, information about native and derived bands, and spatial resolution. The Catalog is also where a user can control the permissions for products they own, allowing you to share imagery with an individual user, an organization, or the general public. Additionally, you can open products in Viewer directly from a products' information page. 

.. ipython:: python

	def catalog_upload(year):

	    # define the product
	    product_id = catalog.add_product(
	            'sar_img_stats:v02',
	            title='SAR VV & VH image stats',
	            description='SAR image statistics (max/min/mean/median/std) from VV & VH backscatter'
	            )['data']['id']

	    # add band id
	    bands=['vv', 'vh']
	    passes = ['DESCENDING', 'ASCENDING', 'BOTH']
	    stats = ['max', 'min', 'mean', 'median', 'std']

	    c = 1
	    for i, band in enumerate(bands):
	        for p in passes:            
	            for stat in stats:
	                band_id = catalog.add_band(
	                    product_id,
	                    '{}_{}_{}'.format(band,stat,p),
	                    jpx_layer=0,
	                    srcfile=0,
	                    srcband=c,
	                    nbits=8,
	                    dtype='Byte',
	                    nodata=0,
	                    data_range=[0, 2**8 - 1],
	                    type='spectral',
	                    default_range=(0,255),
	                    colormap_name='viridis',
	                )['data']['id']
	                c+=1
	            print band_id

***************
 Monitor  
***************
If you use our scalable Tasks API, `Monitor <https://monitor.descarteslabs.com/>`_ allows you to track how tasks are progressing. The interface reports the number of tasks submitted, the number of workers launched, and the status of each task. Upon completion, you can also access each individual task's log to see errors or other console print outs. 