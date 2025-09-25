#from entities.entities import *
from engine.componentmanager import *
from engine.entitymanager import *

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

    C = ComponentTypes # Alias component type enumerator for readability
    attachComponent(ComponentTypes.Location,
                    {"linkedLocations":[]}










































