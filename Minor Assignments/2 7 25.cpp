#include <iostream>
using namespace std;

struct plant
{
    string name;
    string type;
    int waterLevel;
    bool alive;
};

int main()
{
    plant EnochPlant;

    EnochPlant.name = "EnochPlant";
    EnochPlant.type = "Plant from Enoch Garden";
    EnochPlant.waterLevel = 7;
    EnochPlant.alive = false;

    cout << "name: " << EnochPlant.name << endl;
    cout << "type: " << EnochPlant.type << endl;
    cout << "water level: " << EnochPlant.waterLevel << endl;
    if (EnochPlant.alive)
    {
        cout << "plant alive" << endl;
    }
    else
        cout << "ded" << endl;

    EnochPlant.name = "DrMoPlant";
    EnochPlant.type = "Plant from DrMo Garden";
    EnochPlant.waterLevel = 4;
    EnochPlant.alive = true;

    cout << "name: " << EnochPlant.name << endl;
    cout << "type: " << EnochPlant.type << endl;
    cout << "water level: " << EnochPlant.waterLevel << endl;
    if (EnochPlant.alive)
    {
        cout << "plant alive" << endl;
    }
    else
        cout << "plant ded" << endl;

    return 0;
}