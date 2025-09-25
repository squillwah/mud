from dataclasses import dataclass
# ---------------------------
# EntityComponentData:
#  - Structure for storing entities' component data
#  - Stored as 2D list of lists of components, each "list of components" being an entity
#  - EX: Two entites (E1 == components 1+2+4, E2 == components 2+3+4) would be stored like this:
#  - [ [Component1, Component2, None, Component4], 
#      [None, Component2, Component3, Component4] ]
# ---------------------------
# EntityReference:
#  - Structure used to reference single entities
#  - index      = Index of entity's component data in an EntityComponentData list
#  - valid      = Bool, tells if the entity referenced is still valid (not deleted)
#  - container  = Reference to EntityComponentData object the entity's data lives in
# ---------------------------

@dataclass
class EntityComponentData:
    entityList: list[list]          # List of lists of components, each l.o.c. being a single entitiy's data

@dataclass
class EntityReference:
    ID: int                         # Entity's index in an EntityComponentData list
    valid: bool                     # If entity is still alive or has been deleted
    container: EntityComponentData  # Reference to EntityComponentData object the entity's data lives in

