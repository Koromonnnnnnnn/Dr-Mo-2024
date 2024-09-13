#include <iostream>
using namespace std;

bool pointCollision(int x1, int y1, int x2, int y2)
{
    return (x1 == x2) && (y1 == y2);
}

int main()
{

    int x1, y1;
    int x2, y2;
    bool collision;

    cout << "Please enter x1:" << endl;
    cin >> x1;
    cout << "Please enter y1:" << endl;
    cin >> y1;
    cout << "Please enter x2:" << endl;
    cin >> x2;
    cout << "Please enter y2:" << endl;
    cin >> y2;

    if (pointCollision(x1, y1, x2, y2))
    {
        cout << "The points collide." << endl;
        collision = true;
    }
    else
    {
        cout << "The points do not collide." << endl;
        collision = false;
    }

    return 0;
}
