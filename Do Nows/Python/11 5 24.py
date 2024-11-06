import random


def insultComplimet(mode, name):
    if mode == "insult":
        print("You're ugly", name)
    elif mode == "compliment":
        print("You're beautiful", name)
    else:
        print("Invalid argument")


def magicBall(qs):

    replies = [
        "Without a doubt",
        "Ask again later",
        "It is certain",
        "Outlook good",
        "Most likely",
    ]

    print("Question", qs)
    print(random.choice(replies))


def box(h, w):
    for i in range(h):
        print("*" * w)


def avg(a, b, c, d):
    sum = a + b + c + d

    return sum / 4


insultComplimet("insult", "Jaime")
insultComplimet("compliment", "Jaime")

magicBall("Will this code work without bugs?")

box(4, 7)

print("Average:", avg(10, 20, 30, 40))
