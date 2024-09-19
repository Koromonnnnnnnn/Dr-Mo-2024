#include <iostream>
#include <string>
using namespace std;

// READ THIS!
// This is my quiz from last year, but I went through and upgraded all my input into strings and I also made some other improvements.

int main()
{
    int DarthNihilus = 0; // Atra-Manua
    int DarthVader = 0;   // Djem So
    int DarthRevan = 0;   // Ataru
    int DarthSidious = 0; // Juyo
    string input;

    // Question 1
    cout << "If you could learn any lightsaber form, what form would you use?" << endl;
    cout << "Options: Juyo, Atra-Manua, Ataru, Djem-So" << endl;
    cin >> input;
    if (input == "Juyo")
        DarthSidious++;
    else if (input == "Ataru")
        DarthRevan++;
    else if (input == "Atra-Manua")
        DarthNihilus++;
    else if (input == "Djem-So")
        DarthVader++;
    else
        cout << "Sorry, that is not an option." << endl;

    // Question 2
    cout << "If you could choose a planet in the SWU to have been born in, what planet would you pick?" << endl;
    cout << "Options: Naboo, Tatooine, OuterRim, MalachorV" << endl;
    cin >> input;
    if (input == "Naboo")
        DarthSidious++;
    else if (input == "OuterRim")
        DarthRevan++;
    else if (input == "MalachorV")
        DarthNihilus++;
    else if (input == "Tatooine")
        DarthVader++;
    else
        cout << "Sorry, that is not an option." << endl;

    // Question 3
    cout << "What is your preferred lightsaber hilt?" << endl;
    cout << "Options: Kirak's hilt, Self-constructed, Cylindrical hilt, Twin lightsabers" << endl;
    cin >> input;
    if (input == "Twin lightsabers")
        DarthSidious++;
    else if (input == "Cylindrical hilt")
        DarthRevan++;
    else if (input == "Self-constructed")
        DarthNihilus++;
    else if (input == "Kirak's hilt")
        DarthVader++;
    else
        cout << "Sorry, that is not an option." << endl;

    // Question 4
    cout << "How would you most closely describe your personality?" << endl;
    cout << "Options: Stoic, Cautious, Manipulative, Forceful" << endl;
    cin >> input;
    if (input == "Manipulative")
        DarthSidious++;
    else if (input == "Forceful")
        DarthRevan++;
    else if (input == "Cautious")
        DarthNihilus++;
    else if (input == "Stoic")
        DarthVader++;
    else
        cout << "Sorry, that is not an option." << endl;

    // Question 5
    cout << "What do you look for in a Sith apprentice?" << endl;
    cout << "Options: Strength, Determination, Complaisance, HeadStrong" << endl;
    cin >> input;
    if (input == "Strength")
        DarthSidious++;
    else if (input == "HeadStrong")
        DarthRevan++;
    else if (input == "Complaisance")
        DarthNihilus++;
    else if (input == "Determination")
        DarthVader++;
    else
        cout << "Sorry, that is not an option." << endl;

    // Question 6
    cout << "What would be the most alluring reason that you would fall to the Dark Side?" << endl;
    cout << "1: You would never turn, unless you were manipulated to do so." << endl;
    cout << "2: You would never turn, unless you were tortured until your mind was splintered between death and the dark side." << endl;
    cout << "3: Your home planet has been destroyed, and in order to survive you must turn to the dark side." << endl;
    cout << "4: Your significant other is dying, and you are lied to and made to believe that joining the dark side could teach you how to stop her from dying." << endl;
    cin >> input;

    if (input == "1")
        DarthSidious++;
    else if (input == "2")
        DarthRevan++;
    else if (input == "3")
        DarthNihilus++;
    else if (input == "4")
        DarthVader++;
    else
        cout << "Sorry, that is not an option." << endl;

    // Question 7
    cout << "Which force ability would you pick?" << endl;
    cout << "Options: Telekinesis, Valor, Drain, Lightning" << endl;
    cin >> input;
    if (input == "Lightning")
        DarthSidious++;
    else if (input == "Valor")
        DarthRevan++;
    else if (input == "Drain")
        DarthNihilus++;
    else if (input == "Telekinesis")
        DarthVader++;
    else
        cout << "Sorry, that is not an option." << endl;

    // Question 8
    cout << "What gives you power?" << endl;
    cout << "Options: Advanced Strength, Force, Consuming Force Energy, Naturally Gifted At All" << endl;
    cin >> input;
    if (input == "Naturally Gifted At All")
        DarthSidious++;
    else if (input == "Force")
        DarthRevan++;
    else if (input == "Consuming Force Energy")
        DarthNihilus++;
    else if (input == "Advanced Strength")
        DarthVader++;
    else
        cout << "Sorry, that is not an option." << endl;

    // Determine result
    if (DarthSidious >= DarthVader && DarthSidious >= DarthNihilus && DarthSidious >= DarthRevan)
    {
        cout << "You are Darth Sidious!" << endl;
    }
    else if (DarthNihilus >= DarthVader && DarthNihilus >= DarthSidious && DarthNihilus >= DarthRevan)
    {
        cout << "You are Darth Nihilus!" << endl;
    }
    else if (DarthRevan >= DarthVader && DarthRevan >= DarthSidious && DarthRevan >= DarthNihilus)
    {
        cout << "You are Darth Revan!" << endl;
    }
    else if (DarthVader >= DarthRevan && DarthVader >= DarthSidious && DarthVader >= DarthNihilus)
    {
        cout << "You are Darth Vader!" << endl;
    }
    else
    {
        cout << "Test results were not conclusive." << endl;
    }

    return 0;
}
