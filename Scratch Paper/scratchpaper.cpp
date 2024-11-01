#include <iostream>
using namespace std;

void halloweenRating();

int main()
{
    halloweenRating();
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
