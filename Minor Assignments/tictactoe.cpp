#include <iostream>
using namespace std;

int main()
{

    char board[3][3];
    char player = 'X';
    bool endGame = false;

    cout << "Welcome to Tic-Tac-Toe!" << endl;

    while (endGame == false)
    {
        cout << "Player" << player << "'s turn!" << endl
             << endl;

        if (player == 'X')
            player = 'Y';
    }
}