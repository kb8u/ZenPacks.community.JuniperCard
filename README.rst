==============================
ZenPacks.community.JuniperCard README.rst
==============================

About
=====

This ZenPack provides monitoring of chassis-level cards in Juniper Chassis,
and some built in components of the chassis.

A description of the components found, the serial number (if applicable),
and the slot number of the card is displayed under the Components organizer
'Juniper Cards'.  The cards are polled via SNMP for the status of the
alarm LED, and for FRU off-line reason.  Alarm LED generates an error level
event in /Events/HW/JuniperCard, and an FRU off-line reason generates a
warn level event.  A descriptive event summary is generated with an event
tranform in that class.

The Juniper LED status OID is marked as deprecated in the MIB but current
versions of Junos OS still support it as of July 2015.

Requirements
============

Zenoss
------

Zenoss 4 or later. This ZenPack was tested against Zenoss 4.2.4.


Installation
============

Normal Installation (packaged egg)
----------------------------------

Download the `Community Juniper Card ZenPack <http://wiki.zenoss.org/ZenPack:JuniperCard>`_.
Install the zenpack through the zenoss GUI and restart zenoss, or copy the .egg file to your Zenoss server and run the following commands as the zenoss user.

    ::

        zenpack --install ZenPacks.community.JuniperCard-1.0.0-py2.7.egg
        zenoss restart

Developer Installation (link mode)
----------------------------------

If you wish to further develop and possibly contribute back to the
community JuniperCard ZenPack you should clone the git
`repository <https://github.com/kb8u/ZenPacks.community.JuniperCard>`_,
then install the ZenPack in developer mode using the following commands.

    ::

        git clone git://github.com/kb8u/JuniperCard.git
        zenpack --link --install ZenPacks.community.JuniperCard
        zenoss restart


Usage
=====

Installing the ZenPack will add the following items to your Zenoss system.
Apply the community.JuniperCardMap modeler plugin to the device class of
or directly to a specfic Juniper device and model the device.

Modeler Plugin
---------------

- **community.JuniperCardMap** - Juniper Card SNMP modeler plugin.

Monitoring Template
--------------------

- Devices/JuniperCard

Event Class
-------------

- Events/HW/JuniperCard
