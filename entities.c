

// all component types
enum components {
    Descriptor = 0, // Description data
    Player,         // Player data
    Place,          // Place data
    Container,      // Containers data
    Item            // Item data
};

// DESCRIPTOR
// holds name and description of an entity
typedef struct ComponentDescriptor {
    char name[64];
    char desc[512];
} ComponentDescriptor;
void initComponentDescriptor();

// PLAYER
// holds player data for players
typedef struct ComponentPlayer {
    int health;
} ComponentPlayer;
void initComponentPlayer(ComponentPlayer* component);

// PLACE
// holds place data for places
typedef struct ComponentPlace {
    int temperature;
} ComponentPlace;
void initComponentPlace();

// CONTAINER
// holds data for entities which can contain other entities
typedef struct ComponentContainer {
    int num_contents;
    int contents[64]; //@HARDCODE can contain 64 other entity IDs
} ComponentContainer;
void initComponentContainer();

// ITEM
// holds data for item entities
typedef struct ComponentItem {
    int value;
} ComponentItem;
void initComponentItem();
    

void initComponent(void* component, enum components type) {
    switch (type) {
        case Player:
            initComponentPlayer(component);
            break;
        default:
            break;
    }
}


typedef enum actions {
    PickUp = 0,
    LookAround
} actions;

void action1(actions type, int ent1);
void action2(actions type, int ent1, int ent2);
