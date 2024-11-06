import random

def Magic8Ball(question):
    # List of possible responses from the Magic 8 Ball
    responses = [
        "Yes, definitely.",
        "No, not at all.",
        "Ask again later.",
        "Cannot predict now.",
        "Most likely.",
        "Outlook not so good.",
        "Yes, but with some doubt.",
        "My sources say no.",
        "Yes, but it will take time."
    ]
    
    # Print the question and a random response
    print(f"You asked: {question}")
    print("Magic 8 Ball says:", random.choice(responses))

# Example of calling the function:
Magic8Ball("Will this code work without bugs?")

def Box(height, width):
    # Print the box of stars
    for i in range(height):
        print('*' * width)

# Example of calling the function:
Box(4, 7)  # This will print a box 4 tall and 7 wide

def AverageOfFour(a, b, c, d):
    # Calculate the average of the four numbers
    return (a + b + c + d) / 4

# Example of calling the function:
result = AverageOfFour(10, 20, 30, 40)
print("The average is:", result)
