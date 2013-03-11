Introduction
============

This addon register Modernizr_ into Plone's resource registry

version: 2.6.2 (dev)

It provides a way to configure modernizr using the portal_registry.

About Modernizr
===============

Modernizr is an open-source JavaScript library that helps you build the next 
generation of HTML5 and CSS3-powered websites.

Modernizr is a script that detects native CSS3 and HTML5 features available in
the current UA and provides an object containing all features with a true/false
value, depending on whether the UA has native support for it or not.

Modernizr will also add classes to the element of the page, one for each feature
it detects. If the UA supports it, a class like "cssgradients" will be added. 
If not, the class name will be "no-cssgradients". This allows for simple
if-conditionals in your CSS, giving you fine control over the look & feel of
your website.

.. _modernizr: http://www.modernizr.com

How to build or update a new optimized modernizr
================================================

You just have to hit the view /@@plone.app.modernizr.download, you will be
redirect to the download page of modernizr.com with the needed plugins.

So hit the download button to get the modernizr file.

Now to store the js you have two options:

TTW: using plone.resource
-------------------------

* Go to /portal_resources/manage_main
* Add a folder called resource
* Add a file and upload your modernizr js with the id modernizr.custom.js under
  theme/plone.app.modernizr/modernizr.custom.js
* Then go to /portal_registry and configure modernizr resource name to ++theme++plone.app.modernizr/modernizr.custom.js

FS: using your own addon / policy
---------------------------------

* Add you downloaded file to your policy in a resource directory
* Add a registry.xml file to configure modernizr::

  <registry>
    <records interface="plone.app.modernizr.resources.IModernizr">
      <value key="resource">++resource++collective.js.webshims/js/extras/modernizr-custom.js</value>
      <value key="tests">
        <element>canvas</element>
        <element>audio</element>
        <element>video</element>
        <element>input</element>
        <element>inputtypes</element>
        <element>localstorage</element>
        <element>sessionstorage</element>
        <element>geolocation</element>
        <element>shiv</element>
        <element>cssclasses</element>
        <element>addtest</element>
        <element>prefixed</element>
        <element>testprop</element>
        <element>testallprops</element>
        <element>prefixes</element>
        <element>domprefixes</element>
        <element>elem_track</element>
        <element>load</element>
      </value>
    </records>
  </registry>

This way futur maintainer or integrator will be able to provide an updated
version of modernizr without forgeting tests.
