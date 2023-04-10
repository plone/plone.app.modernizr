This repository is archived and read only.

If you want to unarchive it, then post to the [Admin & Infrastructure (AI) Team category on the Plone Community Forum](https://community.plone.org/c/aiteam/55).

===================
plone.app.modernizr
===================


Introduction
============

``plone.app.modernizr`` package provides register `Modernizr`_ into Plone's resource registry

version: 2.6.2 (dev)

It provides a way to configure modernizr using the ``portal_registry`` tool.


About Modernizr
---------------

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


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.resource`` and ``Products.ResourceRegistries`` packages (*You will need enable it to use these packages*)


Features
========

- Provides a browser page ``@@plone.app.modernizr.download`` for download the *Modernizr* js resource.
- Provides the *Modernizr* 2.6.2 version resources.


Installation
============


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``plone.app.modernizr`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plone.app.modernizr


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plone.app.modernizr',
    ],


Enabling
--------

Select and enable the ``plone.app.modernizr`` package from the ``Add-ons``
control panel. That's it!


Usage
=====


How to build or update a new optimized modernizr
------------------------------------------------

You just have to hit the view ``/@@plone.app.modernizr.download``, you will be
redirect to the download page of modernizr.com with the needed plugins.

So hit the download button to get the modernizr file.

Now to store the js you have two options:


TTW: using plone.resource
^^^^^^^^^^^^^^^^^^^^^^^^^

* Go to ``/portal_resources/manage_main``
* Add a folder called ``resource``
* Add a file and upload your modernizr js with the id ``modernizr.custom.js`` under
  the folder called ``theme/plone.app.modernizr/modernizr.custom.js`` 
* Then go to ``/portal_registry`` and configure modernizr resource name to 
  ``++theme++plone.app.modernizr/modernizr.custom.js``


FS: using your own addon / policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Add you downloaded file to your *policy* addon in a ``resource`` directory
* Add a ``registry.xml`` file to configure modernizr:

::

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

This way future maintainer or integrator will be able to provide an updated
version of modernizr without forgetting tests.


Contribute
==========

- Issue Tracker: https://github.com/plone/plone.app.modernizr/issues
- Source Code: https://github.com/plone/plone.app.modernizr


License
=======

The project is licensed under the GPLv2.


Credits
-------

- Plone Foundation.


Amazing contributions
---------------------

- JeanMichel FRANCOIS (toutpt at gmail dot com).
- Jens W. Klein (jk at kleinundpartner dot at).
- Mauro Amico (mauro.amico at gmail dot com).
- Leonardo J. Caballero G. aka macagua (leonardocaballero at gmail dot com).

You can find an updated list of package contributors on https://github.com/plone/plone.app.modernizr/contributors

.. _`Modernizr`: http://www.modernizr.com/
