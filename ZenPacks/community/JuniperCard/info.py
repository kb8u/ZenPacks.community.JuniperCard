################################################################################

__doc__="""info.py

Representation of modules.

"""

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import ThresholdInfo
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.community.JuniperCard import interfaces


class JuniperCardInfo(ComponentInfo):
    implements(interfaces.IJuniperCardInfo)

    slot = ProxyProperty('slot')
    serialNumber = ProxyProperty('serialNumber')
