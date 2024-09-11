#include <iostream>
#include <cmath>
using namespace std;

void equation(float x1, float y1, float x2, float y2)
{
    float distance;
    distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    cout << "The distance between the points is: \n";
    cout << distance;
    cout << "\n";
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
