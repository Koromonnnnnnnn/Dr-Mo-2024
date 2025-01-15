def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        c

def is_palindrome(s):
    # Base case: if the string has 0 or 1 character, it is a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check if the first and last characters match
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])  # Check the substring without first and last characters
    else:
        return False

def print_pattern(n):
    # Base case: if n is 0 or less, stop printing
    if n <= 0:
        return
    # Print n asterisks
    print('*' * n)
    # Recursive case: print n-1 asterisks
    print_pattern(n - 1)
