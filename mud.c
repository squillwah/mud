//#define MAX_ENTITIES 256        // How many entities can the game store?
//#define MAX_NESTED_ENTITIES 64  // How many entities can an entity-component remember?
#include <string.h>

// The idea:
// 
// The game is made of "entities".
// "Entities" are constructed from "components".
//
// "Components" hold data related to a feature of an entity.
// EX: An entity representing a sword will have a weapon component,
//     an entity representing a shopkeep will have a dialogue component.
// 
// "Entities" are interacted with by manipulating data in their "components".
// These "components" are accessed via an entity's "ID",
// which is their index offset in parallel arrays of the component types.

#define MAX_NESTED_ENTITIES 64
typedef struct cPlace {
    int temperature;
    int timeOfDay;
    int numOccupants;
    short occupants[MAX_NESTED_ENTITIES];
} cPlace;
void initComponentPlace(cPlace* component) {
    component->temperature = 0;
    component->timeOfDay = 0;
    component->numOccupants = 0;
    for (int i = 0; i < MAX_NESTED_ENTITIES; i++) 
        component->occupants[i] = 0;
}

#define STR_NAME_SIZE 64
#define STR_DESC_SIZE 1024
typedef struct cDescriptor {
    char name[64];
    char desc[1024];
} cDescriptor;
void initComponentDescriptor(cDescriptor* component) {
    memset(component->name, '\0', STR_NAME_SIZE);
    memset(component->desc, '\0', STR_DESC_SIZE);
}

// Holds flags for attached components of a given entity
typedef struct ECKey { //use bit shifting instead
    int place;
    int descriptor;   
} ECKey;
void initECKey(ECKey* key) {
    key->place = 0;
    key->descriptor = 0;
}

// Holds all the data for every entity in the game
#define MAX_ENTITIES 256
typedef struct EntityData {
    ECKey key[MAX_ENTITIES];
    cPlace componentPlace[MAX_ENTITIES];
    cDescriptor componentDescriptor[MAX_ENTITIES];
} EntityData;

void initEntityData(EntityData* data) {
    for (int entity = 0; entity < MAX_ENTITIES; entity++) {
        initECKey(&(data->key[entity]));
        initComponentPlace(&(data->componentPlace[entity]));
        initComponentDescriptor(&(data->componentDescriptor[entity]));
    }
}

int main() {

    EntityData entities;
    initEntityData(&entities);



    return 0;
}


