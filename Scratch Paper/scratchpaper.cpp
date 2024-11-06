#include <iostream>
#include <cmath> // For floating point division

int main() {
    // Step 1: Declare two variables to store the numbers
    int num1, num2;

    // Step 2: Read the two numbers from user input
    std::cin >> num1 >> num2;

    // Step 3: Handle the case of division
    if (num2 == 0) {
        std::cout << "Cannot divide by zero." << std::endl;
    } else {
        // Perform floating-point division
        double result = static_cast<double>(num1) / num2;
        std::cout << "Result of division: " << result << std::endl;
    }

    // Step 4: Display the numbers in increasing order
    if (num1 < num2) {
        std::cout << num1 << " " << num2 << std::endl;
    } else {
        std::cout << num2 << " " << num1 << std::endl;
    }

    // Step 5: Check if either number is 13
    if (num1 == 13 || num2 == 13) {
        std::cout << "One of the numbers is 13." << std::endl;
    }

    // Step 6: Check if the numbers are odd
    bool isNum1Odd = (num1 % 2 != 0);
    bool isNum2Odd = (num2 % 2 != 0);

    if (isNum1Odd && isNum2Odd) {
        std::cout << "Both numbers are odd." << std::endl;
    } else if (isNum1Odd) {
        std::cout << "The first number is odd." << std::endl;
    } else if (isNum2Odd) {
        std::cout << "The second number is odd." << std::endl;
    } else {
        std::cout << "Neither number is odd." << std::endl;
    }

    return 0;
}
