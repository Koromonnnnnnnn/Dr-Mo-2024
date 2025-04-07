#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream file("words.txt");
    string word;
    int num;

    while (file >> word >> num) {
        for (int i = 0; i < num; i++) {
            cout << word;
        }
        cout << endl;
    }

    file.close();
    return 0;
}
