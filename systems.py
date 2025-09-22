from entities import Entity, Entities
from entities import Components as C
from enum import Enum

class Actions(Enum):
    LOOKAROUND = 0  # the player observes their surroundings
    FOCUS = 1       # the player focuses on an entity 

def PlayerSystem(entities: Entities):
    for player in entities.entityList:  #iterating like this could cause issues if hit None
        if not player.has(C.Player):
            continue
        
        print(f"Hello, {player.get(C.Descriptor).name}.")
        print("LOOKAROUND | FOCUS 'entity' | ENTER 'entity' | PICKUP 'entity'")
        action: str = input("Take Action: ")
    
        match action:
            case "LOOKAROUND":
                local = entities.get(player.get(C.Physical).locationID)
                print(f"You are in {local.get(C.Descriptor).name}.")
                print(local.get(C.Descriptor).desc)
                print("Looking around, you see...")
                for ID in local.get(C.Container).contents:
                    if ID == player.ID:
                        continue
                    if entities.get(ID).has(C.Descriptor):
                        print(f" > {entities.get(ID).get(C.Descriptor).name}")
            case _:
                pass

