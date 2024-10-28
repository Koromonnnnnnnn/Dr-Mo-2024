#include <iostream>
using namespace std;

void dockingCountdown();

void verifyUsername();

int truckWeight(int load);

int getticketPrice(int age);

string schoolzoneSignal(string color);

int main()
{
    dockingCountdown();

    truckWeight(1000);

    schoolzoneSignal("Yellow");

    int age = getticketPrice(16);

    if (age <= 10)
    {
        cout << "Price is $8" << endl;
    }
    else if (age >= 60)
    {
        cout << "Price is $18" << endl;
    }
    else
    {
        cout << "Price is $12" << endl;
    }

    verifyUsername();

    return 0;
}

void dockingCountdown()
{
    for (int i = 20; i >= 0; i -= 3)
    {
        cout << i << endl;
    }
    cout << "Docking Complete" << endl;
}

void verifyUsername()
{
    string username = "CodeMaster123";
    string input;

    while (input != username)
    {
        cout << "What is your username?" << endl;
        cin >> input;
    }
    cout << "Access Granted" << endl;
}

int truckWeight(int load)
{
    if (load <= 1200)
    {
        cout << "Within limit" << endl;
    }
    else
    {
        cout << "Overweight" << endl;
    }

    return load;
}

int getticketPrice(int age)
{
    int price;
    if (age <= 10)
    {
        price = 8;
    }
    else if (age >= 60)
    {
        price = 18;
    }
    else
    {
        price = 12;
    }

    return price;
}

string schoolzoneSignal(string color)
{
    if (color == "Red")
    {
        cout << "Stop" << endl;
    }
    else if (color == "Yellow")
    {
        cout << "Be Ready" << endl;
    }
    else
    {
        cout << "Proceed" << endl;
    }

    return color;
}