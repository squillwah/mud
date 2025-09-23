from enum import Enum
from dataclasses import dataclass
from entities import Entities
from entities import Components as C

class Actions(Enum):
    Observe = "observe"
    Inspect = "inspect"
    Enter = "enter"
    Take = "take"
    Place = "place"

@dataclass
class Action:
    actionType: Actions
    operands: tuple
    executorID: int

# OBSERVE 
# takes group of entities + ID of a location entity + optional tuple of entities to not observe
# prints formatted output of the local surrounding entities contained in the localID entity
def actionObserve(entities: Entities, placeID: int, excludeIDs: tuple = ()):
    output: str = ""
    output +=  "| ---\n"
    output += f"| You are in {entities.get(placeID).get(C.Descriptor).name}.\n"
    output += f"| {entities.get(placeID).get(C.Descriptor).desc}\n"
    output +=  "| \n"
    setpieces: list[str] = []
    otherEnts: list[str] = [] # add more detailed distinctions later
    for ID in entities.get(placeID).get(C.Container).contents:
        if ID in excludeIDs: continue
        if entities.get(ID).has(C.Setpiece): setpieces.append(entities.get(ID).get(C.Setpiece).text)
        if entities.get(ID).has(C.Descriptor): otherEnts.append(entities.get(ID).get(C.Descriptor).name)
    for text in setpieces: output += f"| {text}\n"
    output +=  "| \n"
    output +=  "| Looking around, you see: \n"
    if otherEnts: 
        for name in otherEnts: output += f"|  > {name}\n"
    else: 
        output += "| ...\n"
    output +=  "| ---\n"

    print(output)

# INSPECT
# Takes entities group + entity ID
# Prints formatted display of entity's descriptor
def actionInspect():
    pass

# TAKE
# takes entities group + ID taker + ID of the taken
# moves the taken entity into the container of the taker
def actionTake():
    pass

# Takes a group of entities + an action and executes the related procedure
def executeAction(entities: Entities, action: Action):
    match Action.type:
        case Actions.Observe:
            local = entities.get(action.executorID).get(C.Physical).locationID
            actionObserve(entities, local, (action.executorID,)) 
            pass
        case Actions.Inspect:
            pass
        case Actions.Enter:
            pass
        case Actions.Take:
            pass





