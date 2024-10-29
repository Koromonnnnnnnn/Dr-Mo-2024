#include <iostream>

using namespace std;

void displayThankYouCard()
{
    cout << R"(,

Thank you so much for inviting us to cpp con! Though I didn't get to go, it was still really cool to hear about everything that happened.

Looking forward to going next time!

Best regards,
Jaime/CEC

)" << endl;
}

int main()
{
    displayThankYouCard();
    return 0;
}
