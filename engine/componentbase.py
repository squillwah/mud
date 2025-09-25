from dataclasses import dataclass
from engine.entitybase import EntityReference      # For components which connect entities, Ex: CInventory
from engine.systems.commands import CommandCode    # For the player component, which holds player commands
# --------------------
# CLocation:
#  = Component for entities representing locations
#  - linedLocations 
#     + Dictionary of linked locations
#     + Key is "where" that location is relatively ("North", "South", "Over Yonder")
#     + Value is an EntityReference to the location entity
# --------------------
# CDescriptor:
#  = Component for entities with name + description data
#  - name
#  - description
# --------------------
# CInventory:
#  = Component for entities with inventories
#  - contents
#     + List of EntityReferences to entities inside the inventory
# --------------------
# CAlive:
#  = Component for entities which are living
#  - health
# --------------------
# CPhysical:
#  = Component for entities which can be physically interacted with
#  - weight
# --------------------
# CPlayer:
#  = Component for unique player data
#  - commandQueue
#     + List of player CommandCodes to be processed
# --------------------

@dataclass
class CLocation:
    linkedLocations: dict[str, EntityReference]

@dataclass
class CDescriptor:
    name: str
    description: str

@dataclass
class CInventory:
    contents: list[EntityReference]

@dataclass
class CAlive:
    health: int

@dataclass
class CPhysical:
    weight: int

@dataclass
class CPlayer:
    commandQueue: list[CommandCode]


