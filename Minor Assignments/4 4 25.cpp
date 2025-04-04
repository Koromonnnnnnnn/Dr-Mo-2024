#include <iostream>
using namespace std;

void WHOOOOOOOOOOOOOOOOOOOOO(int *imhungry, int *iwantsushi)
{
    int box = *imhungry;
    *imhungry = *iwantsushi;
    *iwantsushi = box;
}

int main()
{
    int friedrice = 1234;
    int wonton = 5678;

    cout << "one : " << friedrice << endl;
    cout << "two : " << wonton << endl;

    WHOOOOOOOOOOOOOOOOOOOOO(&friedrice, &wonton);

    cout << "on : " << friedrice << endl;
    cout << "two : " << wonton << endl;

    return 0;
}
