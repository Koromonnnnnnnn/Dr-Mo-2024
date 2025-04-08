#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const int SIZE = 5;
int data[SIZE];
string line, num;

int main()
{
    ifstream infile("temps.txt");
    string word;
    int num;

    getline(infile, line);
    infile.close();

    for (int i = 0; i < 5; ++i) {
        int commacheck = line.find(',', 0); 

    }
    

    ofstream outfile("temps.txt");
    outfile.close();
    return 0;
}