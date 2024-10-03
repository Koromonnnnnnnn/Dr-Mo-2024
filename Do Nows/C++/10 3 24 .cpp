#include <iostream>
using namespace std;

class Character
{
private:
    string name;
    int health;
    int defense;

public:
    Character(string x, int y, int z) : name(x), health(y), defense(z) {}

    void takeDmg(int dmg)
    {
        int actualdmg = dmg - defense;
        if (actualdmg > 0)
        {
            health -= actualdmg;
            cout << name << " took " << actualdmg << " damage" << endl;
        }
        if (health <= 0)
        {
            cout << name << " has died" << endl;
            health = 0;
        }
    }

    void stats()
    {
        cout << name << " has " << health << " health" << endl;
    }
};

int main()
{
    Character bossOne("Big Chunk", 2000, 200);
    bossOne.stats();
    bossOne.takeDmg(500);
    bossOne.stats();

    Character bossTwo("Enderman", 1000000, 100000);
    bossTwo.stats();
    bossTwo.takeDmg(200000);
    bossTwo.stats();

    return 0;
}
