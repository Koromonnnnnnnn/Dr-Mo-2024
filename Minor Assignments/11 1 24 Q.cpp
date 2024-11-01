#include <iostream>
using namespace std;

void halloweenRating();
void box();
void booLoop();

int main()
{

    halloweenRating();
    booLoop();
    box();
}

void halloweenRating()
{
    int input;

    cout << "How awesome was your Halloween on a scale of 1-10?" << endl;
    cin >> input;
    if (input < 5)
    {
        cout << "Im sorry it wasn't great" << endl;
    }
    else
    {
        cout << "Im glad you had a good holiday" << endl;
    }
}

void box()
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

void booLoop()
{
    string quit = "q";
    string input;

    while (input != quit)
    {
        cout << "BOO!" << endl;
        cout << "Press any key for another scare, q to quit" << endl;
        cin >> input;
    }
}
