import logging
from Acquisition import aq_base
from zope import component
from StringIO import StringIO
from zope import interface
from zope import schema
from OFS.Image import File
from Products.Five import BrowserView

from plone.registry.interfaces import IRegistry

logger = logging.getLogger('plone.app.modernizr')

TESTS = "-fontface-backgroundsize-borderimage-borderradius-boxshadow-"
TESTS += "flexbox-hsla-multiplebgs-opacity-rgba-textshadow-"
TESTS += "cssanimations-csscolumns-generatedcontent-cssgradients-"
TESTS += "cssreflections-csstransforms-csstransforms3d-csstransitions-"
TESTS += "applicationcache-canvas-canvastext-draganddrop-hashchange-history-"
TESTS += "audio-video-indexeddb-input-inputtypes-localstorage-postmessage-"
TESTS += "sessionstorage-websockets-websqldatabase-webworkers-geolocation-"
TESTS += "inlinesvg-smil-svg-svgclippaths-touch-webgl-iepp-cssclasses-addtest-"
TESTS += "teststyles-testprop-testallprops-hasevent-prefixes-domprefixes-load"


class IModernizr(interface.Interface):
    """Modernizr settings"""

    resource = schema.ASCIILine(title=u"Resource ID",
                    default="++resource++plone.app.modernizr/modernizr.js")

    tests = schema.Tuple(title=u"Tests",
                    description=u"Write only the tests you need.",
                    value_type=schema.ASCIILine(title=u"Test"),
                    default=tuple())


class ModernizrCustomJS(BrowserView):
    """Return the content of the configured resource name"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

        #deps
        self.portal_resgistry = None
        self.settings = None

    def update(self):
        if self.portal_resgistry is None:
            self.portal_resgistry = component.queryUtility(IRegistry)
        if self.settings is None:
            forInterface = self.portal_resgistry.forInterface
            self.settings = forInterface(IModernizr, None)

    def __call__(self):
        self.update()
        if self.settings is None:
            return
        response = self.request.response
        response.setHeader('Content-Type', 'application/javascript')

        resourceid = self.settings.resource
        return self.get_resource_content(resourceid)

    def get_resource_content(self, resourceid):
        """Resources must be a list of resource ids.
        This method return the content of each resources appended in one string
        """
        data = StringIO()
        try:
            resource = self.context.restrictedTraverse(resourceid)
        except KeyError, e:
            logger.error(e)
        if not resource:
            return ""

        if type(aq_base(resource)) == File:
            #is persistent resource
            rname = resource.__name__
            content = "%s" % resource
        else:
            #is browser:resource
            rname = resource.context.__name__
            rpath = resource.context.path
            fic = open(rpath, 'r')
            content = fic.read()
            fic.close()

        data.write(
            u"\n/* plone.app.modernizr: %s */\n" % rname
        )
        data.write(u"\n")
        try:
            content = unicode(content)
        except Exception, e:
            content = unicode(
                content.decode('utf-8'))
        data.write(content)
        data.write(u"\n")
        return data.getvalue()


class PersistentModernizr(object):
    """peristent version of modernizr"""
    interface.implements()


class Download(BrowserView):
    BASE = "http://modernizr.com/download/#"

    def __init__(self, context, request):
        self.context = context
        self.request = request

        self.settings = None

    def update(self):
        if self.settings is None:
            resgistry = component.queryUtility(IRegistry)
            self.settings = resgistry.forInterface(IModernizr, None)

    def __call__(self):
        self.update()
        if not self.settings.tests:
            tests = TESTS
        else:
            tests = '-'.join(self.settings.tests)
        url = self.BASE + tests
        self.request.response.redirect(url)
        return "download"
