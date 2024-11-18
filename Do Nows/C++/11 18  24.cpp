#include <iostream>
using namespace std;

void print_menu();
void religion(int x);
double celsius(double y);

bool loop = true;
char input;
int option;

int main()
{
    print_menu();
    while(loop)
    {
        if (input == 'q'){

        }
        else if (input == 'h'){

        }
        else if (input == 'r'){
            religion(option);
        }
        else if (input == 't'){

        }
        else{
            cout << "invalid input" << endl;
        }
    }
}

void print_menu()
{
    cout << "q: quit" << endl;
    cout << "h: help" << endl;
    cout << "r: info about a religion" << endl;
    cout << "t: temperature conversion"<< endl;
    cout << "Command: ";
}
void religion(int x)
{
    int religionNum;

    cout << "Which religon?";
    cin >> option;

    switch(religionNum)
    {
    case 0:
        cout << "I don't know anything about religion #" << option;
        break;
    case 1:
        cout << "Christianity: 31.2%" << endl;\
        break;
    case 2:
        cout << "" << endl;
        break;
    case 3:
        cout << "" << endl;
        break;
    case 4:
        cout << "" << endl;
        break;
    case 5:
        cout << "" << endl;
        break;
    case 6:
        cout << "" << endl;
        break;
    case 7:
        cout << "" << endl;
        break;
    case 8:
        cout << "" << endl;
        break;
    case 9:
        cout << "" << endl;
        break;
    case 10:
        cout << "" << endl;
        break;
    default:
        cout << "I don't know anything about religion #" << option;
    }
}
double celsius(double y)
{
    return (y - 32) * 5.0 / 9.0;
}