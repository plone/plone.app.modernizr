from Products.CMFCore.utils import getToolByName
PROFILE = 'profile-plone.app.modernizr:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)
