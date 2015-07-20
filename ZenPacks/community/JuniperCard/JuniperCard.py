###########################################################################
#
# written July 7, 2015 by Russell Dwarshuis
#
###########################################################################

__doc="""
Subclass ExpansionCard so a monitoring template for card status
can be applied.
"""
from Globals import DTMLFile
from Globals import InitializeClass

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS, ZEN_VIEW_HISTORY

from Products.ZenModel.ExpansionCard import ExpansionCard

import logging
log = logging.getLogger('JuniperCard')

class JuniperCard(ExpansionCard, ManagedEntity):
    """Juniper Card object"""

    portal_type = meta_type = 'JuniperCard'

    factory_type_information = (
        {
            'id'             : 'JuniperCard',
            'meta_type'      : 'JuniperCard',
            'description'    : "A chassis-level Juniper card or module",
            'product'        : 'ZenModel',
            'factory'        : 'manage_addJuniperCard',
            'immediate_view' : 'viewJuniperCard',
            'actions'        :
            (
                { 'id'            : 'status'
                , 'name'          : 'Status'
                , 'action'        : 'viewJuniperCard'
                , 'permissions'   : (ZEN_VIEW)
                },
                { 'id'            : 'perfConf'
                , 'name'          : 'Template'
                , 'action'        : 'objTemplates'
                , 'permissions'   : (ZEN_CHANGE_SETTINGS)
                },
                { 'id'            : 'viewHistory'
                , 'name'          : 'Modifications'
                , 'action'        : 'viewHistory'
                , 'permissions'   : (ZEN_VIEW_HISTORY)
                },
            )
          },
        )

    def viewName(self):
        return self.snmpindex
    name = viewName

    def manage_deleteComponent(self, REQUEST=None):
        """
        Delete Component
        """
        self.getPrimaryParent()._delObject(self.id)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.device().hw.absolute_url())


InitializeClass(JuniperCard)

