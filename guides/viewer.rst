
Accessing Product Information from Viewer
==========================

Viewing & Hiding Layers 
~~~~~~~~~~~~~~~~~~~~~~~

If you open up this `Viewer link <https://viewer.descarteslabs.com/?config=a68b8760c9f727a431366be7a0a2f515ca79581a>`_ you will find yourself in Northeast Arizona.  


.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

   Data Tab


In the map menu, you should see three layers with 3 of our different product offerings, Landsat-8, Sentinel-2 and GOES-16.  

Your can toggle a layer’s visibility on and off using the button to the left of the layer's name represented by an eye.  You can also use the hotkeys J and K to cycle layers up and down.  To see the all of the keyboard shortcuts, general tips and map toolbar legend click the question mark in the top right corner of the Viewer window.  

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

   Data Tab


Adding a New Layer
~~~~~~~~~~~~~~~~~~

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

   Data Tab

In the map menu click the ‘Add Layer’ button. Find the Landsat-7 Top of Atmospheric Reflection product (‘landsat:LE07:01:RT:TOAR’ ). 

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

   Data Tab

You can manually select the date range, here I’ve set the date range to encompass most of June 2018.  


Changing a Layer’s Opacity
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

   Data Tab


Using the Timeline Slider
~~~~~~~~~~~~~~~~~~~~~~~~~

We’re going to look at GOES-16’s incredible temporal resolution by accessing the timeline slider. To anchor the GOES-16 layer to timeline, click the second button from the right by a layer's name designated by a horizontal line map menu.

Toggling Scene Outlines
~~~~~~~~~~~~~~~~~~~~~~~
To toggle scene outlines, click the third button from the right by a layers name in the map menu.

Turning map labels on and off
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

   Data Tab


Exploring Band combinations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the Viewer window, click the ellipsis beside a layer.
.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

   Data Tab


Next, click “Edit Layer” to access product information and configurations. Inside of the menu, you will see information contained about the selected layer.  Under the “Products” field you will see the product id.  You can use this product id and date range to query for scenes.

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

   Data Tab


Play around with different band combinations (*NIR and SWIR2 are great to look at)


Feature Metadata
~~~~~~~~~~~~~~~~
To find the complete metadata associated with a feature, select the comment box in the top right hand corner of the layer window and click on an image to access the complete metadata associated with a feature.  

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

Searching for Locations
~~~~~~~~~~~~~~~~~~~~~~~
Searching for locations in Viewer utilizes our Places API.  

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

Drawing points, lines and polygons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

You can add polygons, points, squares and line vector features to your Viewer window.  


.. HERE 
Saving &  Loading geojson files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
On the side of your Viewer window, click to save features that were created using the draw function.  You may have to select individual features using .   The features will be saved to your downloads folder as a .geojson.

To load a .geojson into viewer, click . 


Sharing your Viewer Link
~~~~~~~~~~~~~~~~~~~~~~~~
In the top right hand corner of your Viewer window find this icon .  

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button


To get the Shareable Viewer URL click the clipboard icon.

Finding the TMS link for Analytics Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can export layers from Viewer to Analytics Studio.  

Click next to the layer you want to export and then click the option to Export the layer.  


A dialog box will appear that has the option to  copy 3 different types of static urls:  TMS URL, ArcGIS Tile Layer URL and a Tableau TMS XML URL.  

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button


Copy the TMS URL using the clipboard icon.  


Open up `Analytics Studio <https://analytics.descarteslabs.com/>`_

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %
   :alt: add data button

In `Map Settings` expand the options for Base Map.  Choose the option for `Add Custom Basemap.`Paste in your TMS URL into the first field.  

.. figure:: static_images/add-data-button.jpg
   :scale: 50 %

Then click `Add Basemap.`
.. Please see :ref:`Data Types <data-types>` for more on supported data types and formats:

.. - :ref:`Formatting Date Columns <date-format>`
.. - :ref:`Formatting Time Columns <time-format>`
