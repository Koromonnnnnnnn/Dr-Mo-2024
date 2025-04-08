#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    const int SIZE = 5;
    int data[SIZE];
    string line, num_str;
    size_t start_pos = 0;
    long long total = 0;
    int new_temp = 0;
    const string filename = "temps.txt";

    // Read data
    ifstream infile(filename);
    getline(infile, line);
    infile.close();
    for (int i = 0; i < SIZE; ++i) {
        size_t comma_pos = line.find(',', start_pos);
        num_str = line.substr(start_pos, (comma_pos == string::npos) ? string::npos : comma_pos - start_pos);
        data[i] = stoi(num_str); 
        start_pos = (comma_pos == string::npos) ? string::npos : comma_pos + 1;
        total += data[i];
    }

    // Calculate and print average
    cout << "Average: " << static_cast<double>(total) / SIZE << endl;

    // Get new temp
    cout << "New temp: ";
    cin >> new_temp; // Assumes valid integer input

    // Update data
    for (int i = SIZE - 1; i > 0; --i) data[i] = data[i - 1];
    data[0] = new_temp;

    // Write data back
    ofstream outfile(filename);
    for (int i = 0; i < SIZE; ++i) {
        outfile << data[i] << (i < SIZE - 1 ? "," : "");
    }
    outfile.close();

    return 0;
}
