Zenpack for monitoring Juniper card-level status.

Written July 8, 2015 by Russell Dwarshuis

Provides a modeler plugin visible through the GUI as community.Juniper.CardMap
The components get a performance template that polls the Juniper MIBs
jnxLEDState and jnxFruOfflineReason and alerts in /Events/HW/JuniperCard
when an error is detected.

The event class has a transform to change the event summray to indicate the
status as defined in the MIB.
