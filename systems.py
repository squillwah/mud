from entities import Entity, Entities
from entities import Components as C
from enum import Enum

class Actions(Enum):
    LOOKAROUND = 0  # the player observes their surroundings
    FOCUS = 1       # the player focuses on an entity 

#should use id instead of passing entity itself
def generatePlaceDescription(entities: Entities, placeID: int, excludeIDs: tuple = ()) -> str:
    output: str = ""
    output += "| ---\n"
    output += f"| You are in {entities.get(placeID).get(C.Descriptor).name}.\n"
    output += f"| {entities.get(placeID).get(C.Descriptor).desc}\n"
    output += "| \n"

    setpieces: list[str] = []
    otherEnts: list[str] = [] # add more detailed distinctions later

    for ID in entities.get(placeID).get(C.Container).contents:
        if ID in excludeIDs: continue
        if entities.get(ID).has(C.Setpiece):
            setpieces.append(entities.get(ID).get(C.Setpiece).text)
        if entities.get(ID).has(C.Descriptor):
            otherEnts.append(entities.get(ID).get(C.Descriptor).name)

    for text in setpieces:
        output += f"| {text}\n"
    output += "| \n"

    output += "| Looking around, you see: \n"
    if otherEnts:
        for name in otherEnts:
            output += f"|  > {name}\n"
    else:
        output += "| ...\n"

    output += "| ---\n"

    return output



def PlayerSystem(entities: Entities):
    for player in entities.entityList:  #iterating like this could cause issues if hit None, should use a list of ids to stick with design pattern
        if not player.has(C.Player):
            continue
        
        print(f"Hello, {player.get(C.Descriptor).name}.")
        print("LOOKAROUND | FOCUS 'entity' | ENTER 'entity' | PICKUP 'entity'")
        action: str = input("Take Action: ")
    
        match action:
            case "LOOKAROUND":
                localID = player.get(C.Physical).locationID
                
                print(generatePlaceDescription(entities, localID))
                #local = entities.get(player.get(C.Physical).locationID)
                #for ID in local.get(C.Container).contents:
                #    if ID == player.ID:
                #        continue
                #    if entities.get(ID).has(C.Setpiece):
                #        print(entities.get(ID).get(C.Setpiece).text)
                #    elif entities.get(ID).has(C.Descriptor):
                #        print(f" > {entities.get(ID).get(C.Descriptor).name}")
            case _:
                pass

