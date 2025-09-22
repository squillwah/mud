from entities import Entities, Entity#, World
from entities import Components as C
from systems import Systems

#def defineEntityTown(entity: Entity):
#    entity.addComponent(Components.Descriptor)
#    entity.getComponent(Components.Descriptor).name = "Default Town"
#    entity.getComponent(Components.Descriptor).desc = "Description of Default Town"
#
#    entity.addComponent(Components.Place)
#    entity.getComponent(Components.Place).temperature = 69
#
#    entity.addComponent(Components.Container)


# Procedure to create and tie together some entities for a game world
# Ideally this would be done through a json file or something
def defineWorldCalU(world: Entities):
    # create 5 entities in the world
    entityIDs: list[int] = []
    for i in range(0,5):
        # store their IDs
        entityIDs.append(world.create())

    # use their IDs to grab them for local use
    # campus
    campus = world.get(entityIDs[0])
    # eberly hall
    eberly = world.get(entityIDs[1])
    # player
    player = world.get(entityIDs[2])
    # sword
    sword = world.get(entityIDs[3])
    # goblin
    goblin = world.get(entityIDs[4])

    # campus definition
    # description
    campus.add(C.Descriptor, 
               {"name":"CalU Campus", 
                "desc":"Welcome to California University!"})
    # location data (temperature)
    campus.add(C.Place, 
               {"temperature":70})
    # container data (entities on campus)
    campus.add(C.Container, 
               {"contents":[eberly.ID, player.ID]})

    # eberly definition
    # description
    eberly.add(C.Descriptor, 
               {"name":"Eberly Hall",
                "desc":"The Hall of Eberly"})
    # location data (temperature)
    eberly.add(C.Place,
               {"temperature":60})
    # container data (entities inside eberly)
    eberly.add(C.Container,
               {"contents":[goblin.ID, sword.ID]})

    # player definition
    # description
    player.add(C.Descriptor,
               {"name":"The Player",
                "desc":"You"})
    # player data (level)
    player.add(C.Player,
               {"level":2})
    # living creature data (health)
    player.add(C.Alive, 
               {"health":100})
    # container (player inventory)
    player.add(C.Container,
               {"contents":[]})
    # physical (where is the entity in the world)
    player.add(C.Physical,
               {"locationID":campus.ID,
                "weight":175})

    # goblin definition
    # description
    goblin.add(C.Descriptor,
               {"name":"A Goblin",
                "desc":"Goblin Trouble"})
    # living creature data (health)
    goblin.add(C.Alive,
               {"health":50})
    goblin.add(C.Physical,
               {"locationID":eberly.ID,
                "weight":90})

    # sword definition
    # description
    sword.add(C.Descriptor,
              {"name":"Diamond Sword",
               "desc":"Do you like it?"})
    sword.add(C.Physical,
              {"locationID":eberly.ID,
               "weight":10})

def main():


#    townID = earth.createEntity()
#    myEntity = earth.getEntity(townID)
#
#    defineEntityTown(myEntity)
#
#    earth.getEntity(0).debugPrintComponents()

    # create group of entities
    ents = Entities()
    # create systems to operate on entities
    systs = Systems(ents)

    #earth = World()
    defineWorldCalU(ents)

    for e in ents.entityList:
        print()
        e.debugPrintComponents()

    for e in ents.entityList:
        systs.player(e)
        #PlayerSystem(earth, e)

    

    #print("hello!")

    #player = Entity(0)
    #print(player)
    #player.addComponent(Components.Descriptor)
    #player.addComponent(Components.Player)
    #player.addComponent(Components.Place)
    #player.addComponent(Components.Container)
    #
    #player.getComponent(Components.Descriptor).name = "Fred"
    #player.getComponent(Components.Descriptor).desc = "A player named fred"

    #player.components[Components.Descriptor.value].debugPrint()

    #for c in player.components:
    #    print(c)
    #    c.debugPrint()


if __name__ == "__main__":
    main()
    

 
