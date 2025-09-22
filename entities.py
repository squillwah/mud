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

class Entity:
    pass

@dataclass
class Component:
    owner: Entity

@dataclass
class ComponentDescriptor(Component):
    name: str 
    desc: str 

    def debugPrint(self):
        print(self.name)
        print(self.desc)

@dataclass
class ComponentPlayer(Component):
    level: int

    def debugPrint(self):
        print(self.level)

@dataclass
class ComponentPlace(Component):
    temperature: int

    # components shouldn't define functionality
    def generateDescription(self) -> str:
        self.owner.get(Components.Container).contents

    def debugPrint(self):
        print(self.temperature)

@dataclass
class ComponentContainer(Component):
    contents: list[int]

    def debugPrint(self):
        print(self.contents)

@dataclass
class ComponentSetpiece(Component):
    text: str
    
    def debugPrint(self):
        print(self.text)

@dataclass
class ComponentAlive(Component):
    health: int
    
    def debugPrint(self):
        print(self.health)

@dataclass
class ComponentPhysical(Component):
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
                component = ComponentDescriptor(owner=self, **cData) #** notation unpacks dict into named args
            case Components.Player:
                component = ComponentPlayer(owner=self, **cData)
            case Components.Place:
                component = ComponentPlace(owner=self, **cData)
            case Components.Container:
                component = ComponentContainer(owner=self, **cData)
            case Components.Setpiece:
                component = ComponentSetpiece(owner=self, **cData)
            case Components.Alive:
                component = ComponentAlive(owner=self, **cData)
            case Components.Physical:
                component = ComponentPhysical(owner=self, **cData)
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
        self.IDs: list[int] = []
        self._entityList: list[Entity] = []
        self._freeIDs: list[int] = []

    def create(self) -> int:
        entity: Entity 
        if self._freeIDs:
            entity = Entity(self._freeIDs.popleft())
            self.entityList[entity.ID] = entity
        else:
            entity = Entity(len(self.entityList))
            self.entityList.append(entity)
        self.IDs.append(entity.ID)
        return entity.ID

    def destroy(self, ID: int):
        if ID == len(self.entityList)-1:
            self.entityList.pop()
        else:
            self.entityList[ID] = None
            self._freeIDs.append(ID)
        self.IDs.remove(entity.ID)

    def get(self, ID: int):
        return self.entityList[ID]


