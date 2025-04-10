#include <iostream>
using namespace std;

void printBoard(const char board[3][3]);

int main()
{

    char board[3][3];
    char player = 'X';
    bool endGame = false;

    cout << "Welcome to Tic-Tac-Toe!" << endl;

    while (endGame == false)
    {
        printBoard(board);
        cout << "Player" << player << "'s turn!" << endl
             << endl;

        if (player == 'X')
            player = 'Y';
    }
}

void printBoard(const char board[3][3])
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}