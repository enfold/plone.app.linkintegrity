
import OFS.ObjectManager

original = OFS.ObjectManager.ObjectManager.manage_delObjects
# FIXME: Plone needs an api in core
def manage_delObjects(self, ids=None, REQUEST=None):
    if REQUEST is not None and not isinstance(ids, basestring):
        REQUEST.set('link_integrity_events_to_expect', len(ids))
    return original(self, ids, REQUEST)

#OFS.ObjectManager.ObjectManager.manage_delObjects = manage_delObjects
