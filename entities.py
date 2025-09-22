from enum import Enum
from dataclasses import dataclass

class Components(Enum):
    Descriptor = 0  # data for ents with names/descriptions
    Player = 1      # data for ents which are players
    Place = 2       # data for ents which are places
    Container = 3   # data for ents which can contain other ents
    Setpiece = 4    # data for environmental setpieces
    Alive = 5       # data for ents which are alive
    Physical = 6    # data for entities which are physically in the world

@dataclass
class ComponentDescriptor:
    name: str 
    desc: str 

    def debugPrint(self):
        print(self.name)
        print(self.desc)

@dataclass
class ComponentPlayer:
    level: int

    def debugPrint(self):
        print(self.level)

@dataclass
class ComponentPlace:
    temperature: int

    def debugPrint(self):
        print(self.temperature)

@dataclass
class ComponentContainer:
    contents: list[int]

    def debugPrint(self):
        print(self.contents)

@dataclass
class ComponentSetpiece:
    text: str
    
    def debugPrint(self):
        print(self.text)

@dataclass
class ComponentAlive:
    health: int
    
    def debugPrint(self):
        print(self.health)

@dataclass
class ComponentPhysical:
    locationID: int
    weight: int
    
    def debugPrint(self):
        print(self.locationID)
        print(self.weight)

class Entity: 
    def __init__(self, ID: int):
        self.ID: int = ID
        self.components: list = [None]*len(Components)

    def add(self, cType: Components, cData: dict):
        component = None
        match cType:
            case Components.Descriptor:
                component = ComponentDescriptor(**cData) #** notation unpacks dict into named args
            case Components.Player:
                component = ComponentPlayer(**cData)
            case Components.Place:
                component = ComponentPlace(**cData)
            case Components.Container:
                component = ComponentContainer(**cData)
            case Components.Setpiece:
                component = ComponentSetpiece(**cData)
            case Components.Alive:
                component = ComponentAlive(**cData)
            case Components.Physical:
                component = ComponentPhysical(**cData)
            case _:
                print(f"Err: Unkown type '{cType}'")
                return
        self.components[cType.value] = component

    def get(self, cType: Components):
        return self.components[cType.value]

    def has(self, cType: Components):
        return not self.get(cType) == None

    def delete(self, cType: Components):
        self.components[cType.value] = None

    def debugPrintComponents(self):
        print(f"ID: {self.ID}")
        for cType in Components:
            print(cType)
            c = self.get(cType)
            if c != None: c.debugPrint()
            else: print(c)

class Entities:
    def __init__(self):
        self.entityList: list[Entity] = []
        self._freeIDs: list[int] = []

    def create(self) -> int:
        entity: Entity 
        if self._freeIDs:
            entity = Entity(self._freeIDs.popleft())
            self.entityList[entity.ID] = entity
        else:
            entity = Entity(len(self.entityList))
            self.entityList.append(entity)
        return entity.ID

    def destroy(self, ID: int):
        if ID == len(self.entityList)-1:
            self.entityList.pop()
        else:
            self.entityList[ID] = None
            self._freeIDs.append(ID)

    def get(self, ID: int):
        return self.entityList[ID]

#class World: 
#    def __init__(self):
#        # list of every entity in world
#        self.entities: list[Entity] = []
#        # list of all freed entity IDs (self.entities indexes)
#        self.freeIDs: list[int] = []
#
#    # returns ID of entity created
#    def createEntity(self):
#        ent: Entity
#        if len(self.freeIDs) > 0:
#            # create entity with earliest freed ID
#            ent = Entity(self.freeIDs.popleft())
#            self.entities[ent.ID] = ent
#        else:
#            # expand entity list if no IDs are free
#            ent = Entity(len(self.entities))
#            self.entities.append(ent)
#        return ent.ID
#
#    def getEntity(self, entityID: int):
#        return self.entities[entityID]
#
#    def destroyEntity(self, entityID: int):
#        # shorten entity list if at end
#        if entityID == len(self.entities)-1:
#            self.entities.pop()
#        # otherwise nullify entity and add ID to freeID queue
#        else:
#            self.entities[entityID] = None
#            self.freeIDs.append(entityID)


