from engine.entitybase import *
from engine.componentmanager import COMPONENT_COUNT # For allocating element size in EntityComponentData containers

class EntityManager:
    def __init__(self):
        self._ECData = EntityComponentData([])          # List of components for every entity
        self._IDQueue: list[int] = []                   # Queue of free IDs (indexes of destroyed entities) 
        self._references: list[EntityReference] = []    # List of references for every entity existing

    # Create new entity, return reference
    def create(self) -> EntityReference:
        if (self._IDQueue):                                             # Reuse IDs of destroyed entities if available
            ID = self._IDQueue.pop(0)
            self._ECData.entityList[ID] = [None]*COMPONENT_COUNT
        else:                                                           # Otherwise, add entity to end of list w/ new ID
            ID = len(self._ECData.entityList)
            self._ECData.entityList.append([None]*COMPONENT_COUNT)

        entityRef = EntityReference(ID, True, self._ECData)             # Create and return reference to new entity
        self._references.append(entityRef)

        return entityRef

    # Delete entity, invalidate any references
    def destroy(self, e: EntityReference):
        if not (e.container is self._ECData): return    # Don't access entity if its not managed here

        if e.ID == (len(self._ECData.entityList)-1):    # If entity is stored at end of self._entities, shrink the list
            self._ECData.entityList.pop()
        else:                                           # Otherwise, clear the space and add the ID to self._IDQueue
            self._ECData.entityList[e.ID] = None
            self._IDQueue.append(e.ID)

        e.valid = False                                 # Invalidate reference and remove from internal list
        self._references.remove(e)

    # Return true if EntityReference belongs to this manager and is valid 
    def __contains__(self, e: EntityReference):
        return e in self._references



