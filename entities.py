from enum import Enum

class Components(Enum):
    Descriptor = 0  # data for ents with names/descriptions
    Player = 1      # data for ents which are plays
    Place = 2       # data for ents which are places
    Container = 3   # data for ents which can contain other ents

class ComponentDescriptor:
    def __init__(self):
        self.name: str = "blank"
        self.desc: str = "blank"

    def debugPrint(self):
        print("DEBUG: descriptor")
        print(self.name)
        print(self.desc)


class ComponentPlayer:
    def __init__(self):
        self.health: int = 0

    def debugPrint(self):
        print("DEBUG: player")
        print(self.health)


class ComponentPlace:
    def __init__(self):
        self.temperature: int = 0

    def debugPrint(self):
        print("DEBUG: place")
        print(self.temperature)


class ComponentContainer:
    def __init__(self):
        self.contents: list[int] = []

    def debugPrint(self):
        print("DEBUG: container")
        print(self.contents)

class Entity: 
    def __init__(self, ID: int):
        self.ID: int = ID
        self.components: list = [None]*len(Components)

    def addComponent(self, cType: Components):
        component = None
        match cType:
            case Components.Descriptor:
                component = ComponentDescriptor()
            case Components.Player:
                component = ComponentPlayer()
            case Components.Place:
                component = ComponentPlace()
            case Components.Container:
                component = ComponentContainer()
            case _:
                print(f"Err: Unkown type '{cType}'")
                return
        self.components[cType.value] = component

    def getComponent(self, cType: Components):
        return self.components[cType.value]

    def removeComponent(self, cType: Components):
        self.components[cType.value] = None

    def debugPrintComponents(self):
        for cType in Components:
            print(cType)
            c = self.getComponent(cType)

            print(c)
            if c != None:
                c.debugPrint()
            
            print()

class World: 
    def __init__(self):
        # list of every entity in world
        self.entities: list[Entity] = []
        # list of all freed entity IDs (self.entities indexes)
        self.freeIDs: list[int] = []

    # returns ID of entity created
    def createEntity(self):
        ent: Entity
        if len(self.freeIDs) > 0:
            # create entity with earliest freed ID
            ent = Entity(self.freeIDs.popleft())
            self.entities[ent.ID] = ent
        else:
            # expand entity list if no IDs are free
            ent = Entity(len(self.entities))
            self.entities.append(ent)
        return ent.ID

    def getEntity(self, entityID: int):
        return self.entities[entityID]

    def destroyEntity(self, entityID: int):
        # shorten entity list if at end
        if entityID == len(self.entities)-1:
            self.entities.pop()
        # otherwise nullify entity and add ID to freeID queue
        else:
            self.entities[entityID] = None
            self.freeIDs.append(entityID)


