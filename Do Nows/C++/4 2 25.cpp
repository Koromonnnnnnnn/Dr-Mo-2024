#include <iostream>
#include <windows.h>
using namespace std;

int main()
{
    int note;

    cout << "type 1 for a low note, 2 for a medium note, and 3 for a high note." << endl;
    cin >> note;
    if (note <= 1)
        Beep(100, 500);
    else if (note <= 2)
        Beep(200, 500);
    else
        Beep(300, 500);
    
    cout << "how many notes" << endl;
    cin >> note;

    for (int i = 0; i <= note; i++){
        Beep(500, 500);
    }

}