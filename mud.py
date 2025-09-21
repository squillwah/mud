from entities import Entity, Components, World
from systems import PlayerSystem

def defineEntityTown(entity: Entity):
    entity.addComponent(Components.Descriptor)
    entity.getComponent(Components.Descriptor).name = "Default Town"
    entity.getComponent(Components.Descriptor).desc = "Description of Default Town"

    entity.addComponent(Components.Place)
    entity.getComponent(Components.Place).temperature = 69

    entity.addComponent(Components.Container)


# Procedure to create and tie together some entities for a game world
# Ideally this would be done through a json file or something
def defineWorldCalU(world: World):
    # create 5 entities in the world
    entityIDs: list[int] = []
    for i in range(0,5):
        # store their IDs
        entityIDs.append(world.createEntity())

    # use their IDs to grab them for local use
    # campus
    campus = world.getEntity(entityIDs[0])
    # eberly hall
    eberly = world.getEntity(entityIDs[1])
    # player
    player = world.getEntity(entityIDs[2])
    # sword
    sword = world.getEntity(entityIDs[3])
    # goblin
    goblin = world.getEntity(entityIDs[4])

    # campus definition
    # description
    campus.addComponent(Components.Descriptor)
    campus.getComponent(Components.Descriptor).name = "CalU Campus"
    campus.getComponent(Components.Descriptor).desc = "Welcome to California University!"
    # location data (temperature)
    campus.addComponent(Components.Place)
    campus.getComponent(Components.Place).temp = 70
    # container data (entities on campus)
    campus.addComponent(Components.Container)
    # add eberly hall and player IDs to campus entity container
    campus.getComponent(Components.Container).contents.append(eberly.ID)
    campus.getComponent(Components.Container).contents.append(player.ID)

    # eberly definition
    # description
    eberly.addComponent(Components.Descriptor)
    eberly.getComponent(Components.Descriptor).name = "Eberly Hall"
    eberly.getComponent(Components.Descriptor).desc = "The Hall of Eberly"
    # location data (temperature)
    eberly.addComponent(Components.Place)
    eberly.getComponent(Components.Place).temp = 60
    # container data (entities inside eberly)
    eberly.addComponent(Components.Container)
    # add goblin and sword IDs to eberly entity container
    eberly.getComponent(Components.Container).contents.append(goblin.ID)
    eberly.getComponent(Components.Container).contents.append(sword.ID)

    # player definition
    # description
    player.addComponent(Components.Descriptor)
    player.getComponent(Components.Descriptor).name = "The Player"
    player.getComponent(Components.Descriptor).desc = "You."
    # player data (level)
    player.addComponent(Components.Player)
    player.getComponent(Components.Player).level = 2
    # living creature data (health)
    player.addComponent(Components.Alive)
    player.getComponent(Components.Alive).health = 100
    # container (player inventory)
    player.addComponent(Components.Container)
    # physical (where is the entity in the world)
    player.addComponent(Components.Physical)
    player.getComponent(Components.Physical).locationID = campus.ID

    # goblin definition
    # description
    goblin.addComponent(Components.Descriptor)
    goblin.getComponent(Components.Descriptor).name = "A Goblin"
    goblin.getComponent(Components.Descriptor).desc = "Goblin Trouble"
    # living creature data (health)
    goblin.addComponent(Components.Alive)
    goblin.getComponent(Components.Alive).health = 50

    # sword definition
    # description
    sword.addComponent(Components.Descriptor)
    sword.getComponent(Components.Descriptor).name = "Diamond Sword"
    sword.getComponent(Components.Descriptor).desc = "Do you like it?"


def main():

    earth: World = World()

    townID = earth.createEntity()
    myEntity = earth.getEntity(townID)

    defineEntityTown(myEntity)

    earth.getEntity(0).debugPrintComponents()



    defineWorldCalU(earth)

    for e in earth.entities:
        print()
        e.debugPrintComponents()

    for e in earth.entities:
        PlayerSystem(earth, e)

    

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
    

 
