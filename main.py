from engine.componentmanager import *
from engine.entitymanager import *
from game.templates import *

wrld = EntityManager()  # Entity manager for world

room1 = wrld.create()   # Create first room
definePlace(room1)      # Initialize components w/ template 

# Access room1's descriptor component to rename
getComponent(room1, ComponentTypes.Descriptor).name = "The First Room"
getComponent(room1, ComponentTypes.Descriptor).description = "Welcome to The First Room"

creature1 = wrld.create()   # Create some creatures
creature2 = wrld.create()

defineNPC(creature1)  # Initialize w/ templates
defineNPC(creature2)

# Redefine specifics
getComponent(creature1, ComponentTypes.Descriptor).name = "Goblin"
getComponent(creature1, ComponentTypes.Descriptor).name = "A Gross Goblin"
getComponent(creature1, ComponentTypes.Physical).weight = 95
getComponent(creature1, ComponentTypes.Alive).health = 20

getComponent(creature2, ComponentTypes.Descriptor).name = "Elf"
getComponent(creature2, ComponentTypes.Descriptor).name = "An Eloquent Elf"
getComponent(creature2, ComponentTypes.Physical).weight = 170
getComponent(creature2, ComponentTypes.Alive).health = 50

# Place creatures in the room
getComponent(room1, ComponentTypes.Inventory).contents.append(creature1)
getComponent(room1, ComponentTypes.Inventory).contents.append(creature2)

room2 = wrld.create()   # Create second room
definePlace(room2)      # Initialize

# Rename
getComponent(room2, ComponentTypes.Descriptor).name = "The Second Room"
getComponent(room2, ComponentTypes.Descriptor).description = "Welcome to The Second Room"

# Link room1 and room2
getComponent(room1, ComponentTypes.Location).linkedLocations["East"] = room2
getComponent(room2, ComponentTypes.Location).linkedLocations["West"] = room1













#dataclass
#EntityComponentData:
# self.entities = list[list]

#EntityReference
# ID: int
# valid: bool
# location: EntityComponentData



players = EntityManager()

p1 = players.create()
print(p1)
#print(p1.ID)
#print(p1.valid)
#print(p1.location)
#print(p1.location.entityList)

attachComponent(p1, ComponentTypes.Inventory, 
                {"contents":[]})
p1_inventory = getComponent(p1, ComponentTypes.Inventory)
p1_inventory.contents.append(players.create())


print(p1)
print(getComponent(p1, ComponentTypes.Inventory))
detachComponent(p1, ComponentTypes.Inventory)
print(p1)

players.destroy(p1)
print(p1)
#print(p1.ID)
#print(p1.valid)
#print(p1.location)
#print(p1.location.entityList)
#
#locations = EntityManager(save/locations.dat)
#items = EntityManager(save/items.dat)



# saves manager objects?









def defineWorldCalU(manager: EntityManager):
    # Create five entities, storing there references

    campus = manager.create()
    eberly = manager.create()
    player = manager.create()
    goblin = manager.create()
    sword = manager.create()

    attachComponent(campus,                     # Reference to entity
                    ComponentTypes.Location,    # Component Type
                    {"linkedLocations":{}})     # Initial values of component dataclass

    attachComponent(eberly,
                    ComponentTypes.Descriptor,
                    {"name":"eberly",
                     "description":"hall of eberly"})


    print(hasComponent(campus, ComponentTypes.Location))
    print(getComponent(campus, ComponentTypes.Location))
    getComponent(campus, ComponentTypes.Location).linkedLocations["north"] = eberly
    print(getComponent(campus, ComponentTypes.Location))
    detachComponent(campus, ComponentTypes.Location)
    print(hasComponent(campus, ComponentTypes.Location))

    

calu = EntityManager()

defineWorldCalU(calu)







































