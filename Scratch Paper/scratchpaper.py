def quiz1(): #construction quiz
    print("quiz 1 selected1")
   
   
    print("What construction tool are you? Quiz!")
    print("Answer the following questions to find out what type of construction tool you are.\n")

    # Points accumulator
    total_points = 0

    # Question 1
    print("1. How do you approach problems?")
    print("a) I like to tackle them with brute force.")
    print("b) I prefer precision and careful planning.")
    print("c) I improvise and adapt as needed.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  # Hammer
    elif answer == 'b':
        total_points += 20  # Level
    elif answer == 'c':
        total_points += 30  # Saw

    # Question 2
    print("\n2. What's your ideal work environment?")
    print("a) Outdoors, with a lot of room to move around.")
    print("b) Indoors, where I can focus.")
    print("c) Anywhere, as long as I can get the job done.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  # Jackhammer
    elif answer == 'b':
        total_points += 20  # Drill
    elif answer == 'c':
        total_points += 30  # Multi-tool

    # Question 3
    print("\n3. How do you handle stress?")
    print("a) I power through it.")
    print("b) I take a step back and assess the situation.")
    print("c) I adapt quickly and find a solution.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  #  Hammer
    elif answer == 'b':
        total_points += 20  #  Wrench
    elif answer == 'c':
        total_points += 30  #  Pliers


   # Question 4
    print("\n4. How do you prefer to work on tasks?")
    print("a) I work fast and get it done.")
    print("b) I work steadily and take my time.")
    print("c) I work in bursts of energy.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  # Nail Gun
    elif answer == 'b':
        total_points += 20  # Screwdriver
    elif answer == 'c':
        total_points += 30  # Saw

    # Question 5
    print("\n5. What's your preferred role in a team?")
    print("a) The one who gets things started.")
    print("b) The one who fine-tunes and perfects.")
    print("c) The one who fills in where needed.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  # Sledgehammer
    elif answer == 'b':
        total_points += 20  # Level
    elif answer == 'c':
        total_points += 30  # Multi-tool

    # Question 6
    print("\n6. How do you feel about getting your hands dirty?")
    print("a) I love it, bring on the mess.")
    print("b) I don't mind, as long as it gets the job done.")
    print("c) I prefer to keep things neat and clean.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  # Jackhammer
    elif answer == 'b':
        total_points += 20  # Wrench
    elif answer == 'c':
        total_points += 30  # Laser level

    # Question 7
    print("\n7. How do you approach learning new skills?")
    print("a) Jump right in and learn by doing.")
    print("b) Study first, then practice.")
    print("c) Watch others and then try.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  # Power Drill
    elif answer == 'b':
        total_points += 20  # Measuring Tape
    elif answer == 'c':
        total_points += 30  # Circular Saw

    # Question 8
    print("\n8. What's your ideal pace of work?")
    print("a) Fast and furious.")
    print("b) Slow and steady.")
    print("c) Depends on the situation.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  # Nail Gun
    elif answer == 'b':
        total_points += 20  # Level
    elif answer == 'c':
        total_points += 30  # Multi-tool

    # Question 9
    print("\n9. How do you prefer to solve complex problems?")
    print("a) Break them down and smash through.")
    print("b) Analyze every angle before proceeding.")
    print("c) Experiment until something works.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  # Jackhammer
    elif answer == 'b':
        total_points += 20  # Level
    elif answer == 'c':
        total_points += 30  # Angle Grinder

    # Question 10
    print("\n10. What's your reaction to unexpected challenges?")
    print("a) Tackle them head-on without hesitation.")
    print("b) Pause and create a new plan.")
    print("c) Adapt and improvise quickly.")
    answer = input("Your answer (a/b/c): ")
    if answer == 'a':
        total_points += 10  # Sledgehammer
    elif answer == 'b':
        total_points += 20  # Wrench
    elif answer == 'c':
        total_points += 30  # Multi-tool


    # Determine the type of construction tool
    if total_points <= 30:
        tool = "Hammer"
    elif 30 < total_points <= 60:
        tool = "Drill"
    elif 60 < total_points <= 90:
        tool = "Wheelbarrow"
    elif 90 < total_points <= 120:
        tool = "Portable concrete mixer"
    elif 120 < total_points <= 150:
        tool = "Plumb bob"
    elif 150 < total_points <= 180:
        tool = "Jack hammer"
    elif 180 < total_points <= 210:
        tool = "conrete saw"
    elif 210 < total_points <= 240:
        tool = "Plate compactor"
    elif 240 < total_points <= 270:
        tool = "fork lift"
    else:
        tool = "Excavator"

    print(f"You are a {tool}! You're strong, reliable, and always up for a challenge.")
   
quiz1()