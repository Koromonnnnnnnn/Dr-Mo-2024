#include <iostream>
using namespace std;

class Student
{
private:
    string name;
    float mathGrade;
    float scienceGrade;
    float englishGrade;

public:
    Student(string x, float y, float z, float u) : name(x), mathGrade(y), scienceGrade(z), englishGrade(u) {}

    int getAverage()
    {
        float a = (mathGrade + scienceGrade + englishGrade) / 3;
        return a;
    }

    void printReport()
    {
        float a = getAverage();

        cout << name << " Math Grade: " << mathGrade << endl;
        cout << name << " Science Grade: " << scienceGrade << endl;
        cout << name << " English Grade: " << englishGrade << endl;
        cout << name << " Average Grade: " << a << endl;
    }
};

int main()
{
    Student Alice("Alice", 75, 85, 97);
    Alice.getAverage();
    Alice.printReport();

    cout << endl;

    Student Livy("Livy", 54, 95, 20);
    Livy.getAverage();
    Livy.printReport();
    
    return 0;
}