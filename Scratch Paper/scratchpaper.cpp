#include <iostream>
using namespace std;

void print_menu();
void religion(int x);
double celsius(double fahrenheit);

bool loop = true;
char input;
int option;

int main()
{
    while (loop)
    {
        print_menu();
        cin >> input; // Get user input for menu selection
        
        switch (input)
        {
        case 'q': // Quit
            cout << "Exiting program. Goodbye!" << endl;
            loop = false;
            break;

        case 'h': // Help
            cout << "Help: Choose an option to learn more or perform an action." << endl;
            break;

        case 'r': // Info about a religion
            cout << "Enter a number for the religion (1-10): ";
            cin >> option;
            religion(option);
            break;

        case 't': // Temperature conversion
        {
            double fahrenheit;
            cout << "Enter temperature in Fahrenheit: ";
            cin >> fahrenheit;
            double result = celsius(fahrenheit);
            cout << "Temperature in Celsius: " << result << "°C" << endl;
            break;
        }

        default:
            cout << "Invalid input, please try again." << endl;
        }
    }
    return 0;
}

void print_menu()
{
    cout << "\nMenu:\n";
    cout << "q: Quit\n";
    cout << "h: Help\n";
    cout << "r: Info about a religion\n";
    cout << "t: Temperature conversion\n";
    cout << "Command: ";
}

void religion(int x)
{
    switch (x)
    {
    case 1:
        cout << "Christianity: 31.2%" << endl;
        break;
    case 2:
        cout << "" << endl; // Placeholder
        break;
    case 3:
        cout << "" << endl; // Placeholder
        break;
    case 4:
        cout << "" << endl; // Placeholder
        break;
    case 5:
        cout << "" << endl; // Placeholder
        break;
    case 6:
        cout << "" << endl; // Placeholder
        break;
    case 7:
        cout << "" << endl; // Placeholder
        break;
    case 8:
        cout << "" << endl; // Placeholder
        break;
    case 9:
        cout << "" << endl; // Placeholder
        break;
    case 10:
        cout << "" << endl; // Placeholder
        break;
    default:
        cout << "I don't know anything about religion #" << x << endl;
    }
}

double celsius(double fahrenheit)
{
    return (fahrenheit - 32) * 5.0 / 9.0;
}
