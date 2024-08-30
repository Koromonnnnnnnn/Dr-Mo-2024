#include <iostream>
using namespace std;

string choice;
bool loop = true;

int counter = 0;

int main()
{

    for (int j = 5; j <= 85; j += 10)
        cout << j << " ";

    cout << endl;

    while (counter <= 80)
    {
        counter += 5;
        cout << counter << " ";
    }

    cout << endl;

    while (loop != false)
    {
        cout << "FORGLE" << endl;
        cin >> choice;
        if (choice == "BOOP" || choice == "boop")
        {
            loop = false;
            break;
        }
    }
}