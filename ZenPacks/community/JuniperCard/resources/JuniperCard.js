/* show the same fields as the stock JuniperCard GUI
 * written 7/7/2015 by Russell Dwarshuis
*/

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}


ZC.JuniperCardPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'JuniperCard',
            autoExpandColumn: 'name',
            fields: [
                {name: 'uid'},
                {name: 'slot'},
                {name: 'name'},
                {name: 'serialNumber'},
                {name: 'locking'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'slot',
                dataIndex: 'slot',
                header: _t('Slot'),
                width: 80
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 80
            },{
                id: 'serialNumber',
                dataIndex: 'serialNumber',
                header: _t('Serial Number'),
                width: 110
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons
            }]
        });
        ZC.JuniperCardPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('JuniperCardPanel',ZC.JuniperCardPanel);
ZC.registerName('JuniperCard', _t('Juniper Card'), _t('Juniper Cards'));

})();

