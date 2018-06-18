============
Descartes Labs Web Interfaces 
============

The Descartes Labs programmatic APIs have accompanying web interfaces to allow for wider and more user friendly access. Some of those web interfaces are described below. 

***************
 Viewer 
***************
The `Descartes Labs Viewer <viewer.descarteslabs.com>`_ interface sits on top of our Metadata API and provides full visual access to your access-granted products. By default, the Landsat 8 Real Time product opens focused on your location (if available). You can choose to add new layers, or remove, toggle, and edit currently loaded layers. The edit option allows you to query the dataset by time and cloud fraction as well as visualize different band combinations. 

** Generate a Static XYZ Layer ** 

XYZ is a `tiling protocol <https://en.wikipedia.org/wiki/Tiled_web_map>`_  that can be used by a mapping client like ArcGIS or QGIS to access image data. The `Descartes Labs Viewer <viewer.descarteslabs.com>`_ allows users to generate a static XYZ URL of imagery that can be imported into other mapping environments. To generate an XYZ URL, you click the ellipsis next to the layer of interest, and select "Create static XYZ". The URL will appear in the drop-down menu of your saved Static XYZ URLs. 

.. figure:: https://cdn.descarteslabs.com/docs/static_xyz.png

Once you have a static XYZ URL, you can add it to any number of map applications that support XYZ protocol.  Here is more information about how to add a XYZ layer to `QGIS <https://www.spatialbias.com/2018/02/qgis-3.0-xyz-tile-layers/>`_ and `ArcGIS <https://gis.stackexchange.com/questions/174569/adding-custom-web-tile-layer-to-arcmap>`_.

******************
 GeoVisual Search   
******************

GeoVisual Search 

***************
 Catalog 
***************

***************
 Monitor  
***************