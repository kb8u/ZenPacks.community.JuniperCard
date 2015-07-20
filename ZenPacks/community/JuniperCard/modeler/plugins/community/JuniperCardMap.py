################################################################################
#
# This program is part of the JuniperCard Zenpack for Zenoss.
# Copyright (C) 2015 Russell Dwarshuis
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__ =\
"""Walk Juniper jnxContentsTable to find fans, power supplies, routing engines,
etc. that are part of or plugged into a Juniper Chassis"""

from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import MultiArgs


class JuniperCardMap(SnmpPlugin):
    "Map Juniper cards to the python class for them"

    modname = "ZenPacks.community.JuniperCard.JuniperCard"
    relname = "cards"
    compname = "hw"

    snmpGetTableMaps = ( GetTableMap('jnxContentsTable',
                                     '.1.3.6.1.4.1.2636.3.1.8.1',
                                     { '.6': 'jnxContentsDescr',
                                       '.7': 'jnxContentsSerialNo' } ),)


    def process(self, device, results, log):
        """ Run SNMP queries, process returned values from jnxContentsTable """

        log.info('Starting process() for modeler JuniperCard')

        getdata, tabledata = results
        rm = self.relMap()

        jnxContentsTable = tabledata.get('jnxContentsTable')
        if not jnxContentsTable:
            log.info('No data returned from jnxContentsTable')
            return

        for snmpindex, card in jnxContentsTable.iteritems():
            log.info('Found card %s' % jnxContentsTable[snmpindex]['jnxContentsDescr'])
            om = self.objectMap()
            om.id = self.prepId(snmpindex)
            om.title = jnxContentsTable[snmpindex]['jnxContentsDescr']
            om.snmpindex = snmpindex
            om.serialNumber = jnxContentsTable[snmpindex]['jnxContentsSerialNo']
            om.slot = int(snmpindex.split('.')[0])
            om.monitor = True
            rm.append(om)

        return rm
