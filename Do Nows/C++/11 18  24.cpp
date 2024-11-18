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

    while (loop)
    {
        print_menu();
        cin >> input;

        if (input == 'q')
        {
            loop = false;
        }
        else if (input == 'h')
        {
            print_menu();
            cin >> input;
        }
        else if (input == 'r')
        {
            cout << "Which religon? ";
            cin >> option;
            religion(option);
        }
        else if (input == 't')
        {
            double f;
            cout << "Farenheit: ";
            cin >> f;
            getchar();
            double r = celsius(f);
            cout << f << " Farenheit is " << r << " Celsius" << endl;
        }
        else
        {
            cout << "invalid command" << endl;
        }
    }
    return 0;
}

void print_menu()
{
    cout << "q: quit" << endl;
    cout << "h: help" << endl;
    cout << "r: info about a religion" << endl;
    cout << "t: temperature conversion" << endl;
    cout << "Command: ";
}
void religion(int x)
{
    switch (x)
    {
    case 0:
        cout << "I don't know anything about religion #" << option;
        break;
    case 1:
        cout << "Christianity: 31.2%" << endl;
        break;
    case 2:
        cout << "Islam: 24.1%" << endl;
        break;
    case 3:
        cout << "Secular/Nonreligious/Agnostic/Atheist: 16%" << endl;
        break;
    case 4:
        cout << "Hinduism: 15.1%" << endl;
        break;
    case 5:
        cout << "Buddhism: 6.9%" << endl;
        break;
    case 6:
        cout << "Chinese traditional religion: 5.5%" << endl;
        break;
    case 7:
        cout << "Ethnic religions: 4.19%" << endl;
        break;
    case 8:
        cout << "African traditional religions: 1.4%" << endl;
        break;
    case 9:
        cout << "Sikhism: 0.32%" << endl;
        break;
    case 10:
        cout << "Spiritsm: 0.21%" << endl;
        break;
    default:
        cout << "I don't know anything about religion #" << option;
    }
}
double celsius(double y)
{
    return (y - 32) * 5.0 / 9.0;
}