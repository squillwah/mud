from entities import Entity, Entities
from entities import Components as C
from actions import Action, Actions, actionObserve

# Helper func to pick entity IDs out of list by their descriptor names
def findByDescriptorName(entities: Entities, IDList: int, name: str) -> int:
    foundID = -1
    for ID in IDList: 
        if entities.get(ID).has(C.Descriptor):
            if entities.get(ID).get(C.Descriptor).name == name:
                foundID = ID
                break;
    return foundID

# Process input commands, add actions to player action queue
def InputSystem(entities: Entities):
    for ID in entities.IDs:
        # skip if not a player entity
        if not entities.get(ID).has(C.Player): continue

        # input with prompt
        player = entities.get(ID)
        print(f"Hello, {player.get(C.Descriptor).name}.")
        print("OBSERVE | FOCUS 'entity' | ENTER 'entity' | PICKUP 'entity'")
        action: str = input("Take Action: ")

        # divide input string into words
        command = action.lower().split()
        if not command: continue # if no words, skip
        #if len(command) > 1:

        # match first word to known actions
        match command[0]:
            case Actions.Observe.value:
                if len(command) != 1: continue # skip if bad # operands for action
                player.get(C.Player).actionQueue.append((Actions.Observe,))
            case Actions.Inspect.value:
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
                actionObserve(entities, local, (player.ID,)) #placeholder, should be done through execute in Actions
                #print(generatePlaceDescription(entities, local, (player.ID,)))
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

