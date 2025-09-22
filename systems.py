from entities import Entity, Entities
from entities import Components as C
from enum import Enum

class Actions(Enum):
    Observe = "observe" # the player observes their surroundings
    Focus = "focus"     # the player focuses on an entity 
    Enter = "enter"     # the player enters an entity
    Take = "take"       # the player takes an entity

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


# Process input commands, add actions to player action queue
def InputSystem(entities: Entities):
    for ID in entities.IDs:
        if not entities.get(ID).has(C.Player):
            continue

        player = entities.get(ID)
        print(f"Hello, {player.get(C.Descriptor).name}.")
        print("OBSERVE | FOCUS 'entity' | ENTER 'entity' | PICKUP 'entity'")
        action: str = input("Take Action: ")

        command = action.lower().split()
        match command[0]:
            case Actions.Observe.value:
                player.get(C.Player).actionQueue.append((Actions.Observe,))
            case Actions.Focus.value:
                player.get(C.Player).actionQueue.append((Actions.Focus, ID))
            case _:
                pass

# Process player action queues
def PlayerSystem(entities: Entities):
    for ID in entities.IDs:  
        if not entities.get(ID).has(C.Player):
            continue

        player = entities.get(ID)
        if not player.get(C.Player).actionQueue:
            continue

        action = player.get(C.Player).actionQueue.pop(0)

        match action[0]:
            case Actions.Observe:
                local = player.get(C.Physical).locationID
                print(generatePlaceDescription(entities, local, (player.ID,)))
            case Actions.Focus:
                focus = entities.get(action[1])
                print("| ---")
                print(f"| {focus.get(C.Descriptor).name}")
                print(f"|  {focus.get(C.Descriptor).desc}")
                print("| ---")
    
#        match action:
#            case "LOOKAROUND":
#                local = entities.get(player).get(C.Physical).locationID
#                print(generatePlaceDescription(entities, local, [player]))
#            case _:
#                pass

