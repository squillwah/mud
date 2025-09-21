from entities import Entity, Components, World
from enum import Enum

class Actions(Enum):
    LOOKAROUND = 0  # the player observes their surroundings
    FOCUS = 1       # the player focuses on an entity 



# Processes all functions related to entitis with the 'Player' component
def PlayerSystem(world: World, player: Entity):
    # Skip if entity isn't a player
    if player.getComponent(Components.Player) == None:
        return

    # Take in player actions
    print(f"Hello, {player.getComponent(Components.Descriptor).name}.")
    print("LOOKAROUND | FOCUS 'entity' | ENTER 'entity' | PICKUP 'entity'")
    action: str = input("Take Action: ")

    match action:
        case "LOOKAROUND":
            location = world.getEntity(player.getComponent(Components.Physical).locationID)
            print(f"You are in {location.getComponent(Components.Descriptor).name}.")
            print(location.getComponent(Components.Descriptor).desc)

            print("Looking around, you see... ")
            for entityID in location.getComponent(Components.Container).contents:
                if entityID == player.ID:
                    continue
                entity = world.getEntity(entityID)
                if entity.getComponent(Components.Descriptor) != None:
                    print(f" > {entity.getComponent(Components.Descriptor).name}")
        case _:
            pass

       
    


    
