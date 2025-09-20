typedef enum components {
    Player = 0,
    Place,
    Item
} components;

typedef struct ComponentPlayer {
    int health;
} ComponentPlayer;
void initComponentPlayer();

typedef enum actions {
    PickUp = 0,
    LookAround
} actions;

void action1(actions type, int ent1);
void action2(actions type, int ent1, int ent2);
