#include <iostream>

// Function to calculate the factorial of n
int factorial(int n) {
    if (n <= 1) {
        return 1; // Base case: factorial(0) = factorial(1) = 1
    }
    return n * factorial(n - 1); // Recursive case
}

// Function to calculate the sum of digits of n
int sumOfDigits(int n) {
    if (n == 0) {
        return 0; // Base case: the sum of digits of 0 is 0
    }
    return (n % 10) + sumOfDigits(n / 10); // Recursive case
}

// Function to print the binary representation of n
void printBinary(int n) {
    if (n > 1) {
        printBinary(n / 2); // Recursive case
    }
    std::cout << (n % 2); // Print the least significant bit
}

int main() {
    int number = 5; // Example input for factorial
    std::cout << "Factorial of " << number << " is " << factorial(number) << std::endl;

    number = 1234; // Example input for sum of digits
    std::cout << "Sum of digits of " << number << " is " << sumOfDigits(number) << std::endl;

    number = 10; // Example input for binary representation
    std::cout << "Binary representation of " << number << " is ";
    printBinary(number);
    std::cout << std::endl;

    return 0;
}
