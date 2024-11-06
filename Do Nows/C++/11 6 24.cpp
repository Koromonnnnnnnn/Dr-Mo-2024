#include <iostream>
using namespace std;

int main()
{
    double num1, num2;

    cout << "A couple of numbers, if you please:";
    cin >> num1 >> num2;

    double anws = num1 / num2;

    if (num1 == 0)
    {
        cout << "Division of 0 by " << num2 << ": nope!" << endl;
    }
    else if (num2 == 0)
    {
        cout << "Division of 0 by " << num1 << ": nope!" << endl;
    }
    else
    {
        cout << "Division of " << num1 << " by " << num2 << ": " << anws << endl;
    }

    if (num1 < num2)
    {
        cout << "In order: " << num1 << " " << num2 << endl;
    }
    else if (num1 > num2)
    {
        cout << "In order: " << num2 << " " << num1 << endl;
    }
    else
    {
        cout << "Error putting numbers in order" << endl;
    }

    if (num1 == 13)
    {
        cout << "Bad luck!" << endl;
    }
    else if (num2 == 13)
    {
        cout << "Bad luck!" << endl;
    }

    return 0;
}