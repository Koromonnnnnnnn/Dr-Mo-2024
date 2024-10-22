#include <iostream>
#include <cmath>
using namespace std;

// Broken Spicy Code attempt
// int factorialCalculator(int n) // Broken Spicy Code attempt
//{
// return n * factorialCalculator(n - 1);
//}

double area(double length, double width)
{
    return length * width;
}

bool isPrime(int n)
{
    int num = n-1;
    while (num > 1)
    {
        if (n % num == 0)
        {
            cout << num <<  " divided evenly" << endl;
            return false;
            break;
        }
        else
        {
            cout << "didn't divide evenly" << endl;
            break;
        }
        num--;
    }
    return true;
}

int main()
{

    cout << area(5, 2) << endl;
    cout << isPrime(13);
}