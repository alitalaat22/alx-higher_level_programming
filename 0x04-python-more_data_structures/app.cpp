#include <iostream>
using namespace std;
int main()
{
    int age;
    cout << "Hello World\n";
    cout << "Hey Mohammed\n";
    cout << "Please Enter your age\n";
    while (true)
    {
        cin >> age;
        if (age == 25)
        {
            cout << "Correct Answer\n";
            cout << "your age is : " << age;
            break;
        }
        else
        {
            // do
            // {
                cout << "ReType your age\n";
            // } while (age != 25);
        }
    }

    return 0;
}
