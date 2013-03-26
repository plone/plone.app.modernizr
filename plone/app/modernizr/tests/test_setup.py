from plone.app.modernizr.tests import base

OLD_JS = 'modernizr.js'
JS = '++resource++plone.app.modernizr.custom.js'
PROFILE = 'plone.app.modernizr:default'

class TestIntegration(base.TestCase):

    def test_jsregistry(self):
        jsregistry = self.portal.portal_javascripts
        modernizr = jsregistry.getResource(OLD_JS)
        self.failUnless(not modernizr.getEnabled())
        new_modernizr = jsregistry.getResource(JS)
        self.failUnless(new_modernizr.getEnabled())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    return base.build_test_suite((TestIntegration,))
