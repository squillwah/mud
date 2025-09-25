from enum import Enum
from engine.componentbase import *
from engine.entitybase import EntityReference   # To access entity of components being modified
# --------------------
# ComponentTypes:
#  = Enum which holds every component type
#  = Associated integer is index of component in an EntityComponentData entityList element
# --------------------
# component(c: Types, init: dict):
#  = Function for creating component instances
#  = Returns component of type 'c' initialized with 'init'
#  - c:
#     + Component type enum constant
#  - init:
#     + Dictionary of initial values (unique to each component type)
# --------------------
# attachComponent
# --------------------
# detachComponent
# --------------------
# hasComponent
# --------------------
# getComponent
# --------------------

# Constant for every component type
class ComponentTypes(Enum):
    Location    = 0
    Descriptor  = 1
    Inventory   = 2
    Alive       = 3
    Physical    = 4
    Player      = 5
COMPONENT_COUNT = 6

# Get an instance of a component type initialzed to 'init'
def component(c: ComponentTypes, init: dict):
    match c:
        case ComponentTypes.Location:
            return CLocation(**init)
        case ComponentTypes.Descriptor:
            return CDescriptor(**init)
        case ComponentTypes.Inventory:
            return CInventory(**init)
        case ComponentTypes.Alive:
            return CAlive(**init)
        case ComponentTypes.Physical:
            return CPhysical(**init)
        case ComponentTypes.Player:
            return CPlayer(**init)
        case _:
            print("Err: Bad Component Type")
    return None

# Add a component to an enity
def attachComponent(e: EntityReference, c: ComponentTypes, init: dict):
    if not e.valid: print("Err: Bad Entity Reference")                  # Check reference validity
    elif not (c in ComponentTypes): print("Err: Bad Component Type")    # Check component validity
    else: e.container.entityList[e.ID][c.value] = component(c, init)    # Create and attach component

# Remove a component from an entity
def detachComponent(e: EntityReference, c: ComponentTypes):
    if not e.valid: print("Err: Bad Entity Reference")
    elif not (c in ComponentTypes): print("Err: Bad Component Type")
    else: e.container.entityList[e.ID][c.value] = None

# Check if entity contains a component
def hasComponent(e: EntityReference, c: ComponentTypes):
    has = False
    if not e.valid: print("Err: Bad Entity Reference")
    elif not (c in ComponentTypes): print("Err: Bad Component Type")
    else: has = e.container.entityList[e.ID][c.value] != None
    return has

# Access a component of an entity
def getComponent(e: EntityReference, c: ComponentTypes):
    component = None
    if not e.valid: print("Err: Bad Entity Reference")
    elif not (c in ComponentTypes): print("Err: Bad Component Type")
    else: component = e.container.entityList[e.ID][c.value]
    return component
