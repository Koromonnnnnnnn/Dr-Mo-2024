#include <iostream>
using namespace std;

int areaCalculator()
{
    int B;
    int H;

    cout << "Enter base: ";
    cin >> B;
    cout << "Enter height: ";
    cin >> H;

    int Area = (B * H) / 2;

    return Area;
}

int main()
{
    int Area = areaCalculator();
    cout << "The area is" << Area << endl;

    return 0;
}
