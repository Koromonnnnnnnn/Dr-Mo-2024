def factorial(s):
    if s == 0 or s == 1:
        return 1
    else:
        return s * factorial(s - 1)


print(factorial(5))  # 120


def is_palindrome(s, start, end):
    if start >= end:
        return True

    if s[start] == s[end]:
        return is_palindrome(s, start + 1, end - 1)
    return False


print(is_palindrome("amanaplanacanalpanama", 0, len("amanaplanacanalpanama") - 1))
print(is_palindrome("hello", 0, len("hello") - 1))


def print_pattern(n):
    if n >= 0:
        for i in range(n):
            print("*", end="")
        print()

        return print_pattern(n - 1)


print_pattern(5)
