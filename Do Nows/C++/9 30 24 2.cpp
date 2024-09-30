#include <iostream>
using namespace std;

int sumDigits(int n)
{
    n = abs(n);
    int sum = 0;
    while (n)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

double area(double length, double width)
{
    return length * width;
}

bool isPrime(int n)
{
    if (n < 2)
        return false;
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main()
{
    double a = area(5, 20);
    cout << a << endl;

    int s = sumDigits(25);
    cout << s << endl;

    bool i = isPrime(5);
    if (i == true)
    {
        cout << "Prime" << endl;
    }
    else
    {
        cout << "Not prime" << endl;
    }

    return 0;
}