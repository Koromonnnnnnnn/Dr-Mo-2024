#include <iostream>
using namespace std;
// global variables go here

void equation(float x1, float y1, float x2, float y2)
{
    float xmid;
    float ymid;
    xmid = (x1 + x2) / 2;
    ymid = (y1 + y2) / 2;
    cout << "The midpoint (x,y) is: \n";
    cout << "x = ";
    cout << xmid;
    cout << "\n";
    cout << "y = ";
    cout << ymid;
}

int main()
{
    float x1;
    float x2;
    float y1;
    float y2;
    cout << "Please input x1" << endl;
    cin >> x1;
    cout << "Please input x2" << endl;
    cin >> x2;
    cout << "Please input y1" << endl;
    cin >> y1;
    cout << "Please input y2" << endl;
    cin >> y2;

    equation(x1, y1, x2, y2);
}