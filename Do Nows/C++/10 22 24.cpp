#include <iostream>
#include <cmath>
using namespace std;

int factorialCalculator(int n)
{

    return n * factorialCalculator(n - 1);
}

int main()
{

    int c = factorialCalculator(5);
    cout << c;
}