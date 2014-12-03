from collective.grok import gs
from Sinar.Theme import MessageFactory as _

@gs.importstep(
    name=u'Sinar.Theme', 
    title=_('Sinar.Theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('Sinar.Theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
