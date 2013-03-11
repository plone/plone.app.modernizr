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

    tests = schema.Tuple(title=u"Tests",
                    description=u"Write only the tests you need.",
                    value_type=schema.ASCIILine(title=u"Test"),
                    default=tuple())


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
        return ""
