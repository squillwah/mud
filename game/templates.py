from engine.entitybase import EntityReference
from engine.componentmanager import *

def definePlace(place: EntityReference):
    # Places are locations with inventories which can be described

    initLocation    = {"linkedLocations" : {}}
    initDescriptor  = {"name"            : "Template Place",
                       "description"     : "Description of Place Template"}
    initInventory   = {"contents"        : []}

    attachComponent(place, ComponentTypes.Location, initLocation)
    attachComponent(place, ComponentTypes.Descriptor, initDescriptor)
    attachComponent(place, ComponentTypes.Inventory, initInventory)


def defineNPC(npc: EntityReference):
    # NPCs are physical living entities with inventories which can be described

    initDescriptor  = {"name"        : "Template NPC",
                       "description" : "Description of Template NPC"}
    initInventory   = {"contents"    : []}
    initPhysical    = {"weight"      : 200}
    initAlive       = {"health"      : 100}

    attachComponent(npc, ComponentTypes.Descriptor, initDescriptor)
    attachComponent(npc, ComponentTypes.Inventory, initInventory)
    attachComponent(npc, ComponentTypes.Physical, initPhysical)
    attachComponent(npc, ComponentTypes.Alive, initAlive)


