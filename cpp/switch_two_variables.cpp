// Coud you switch two variables without an extra variable ?
// Challange accepted!
#include <iostream>
using namespace std;

int main()
{
    int a = 10, b = 20;
    cout << "a is " << a << ", b is " << b << endl;
    a = a + b;
    b = a - b;
    a = a - b;
    cout << "after switching: \n"
         << "a is " << a << ", b is " << b << endl;
    return 0;
}