#include <iostream>
#include <windows.h>
using namespace std;

void RandomBeeps();

int main()
{
    int note;

    cout << "type 1 for a low note, 2 for a medium note, and 3 for a high note." << endl;
    cin >> note;

    if (note == 1)
        Beep(200, 400);
    if (note == 2)
        Beep(400, 400);
    if (note == 3)
        Beep(800, 400);

    cout << "how many notes do you want to play?" << endl;
    cin >> note; // puts user key press into note
    for (int i = 0; i < note; i++)
        Beep(400, 400);

    RandomBeeps();
}

void RandomBeeps()
{
    int num = rand() % 100;
    if (num < 20)
        Beep(300, 300);
    else if (num < 50)
        Beep(600, 600);
    else
        Beep(900, 900);
}