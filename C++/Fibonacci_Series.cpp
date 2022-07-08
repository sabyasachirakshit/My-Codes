//?The objective of this C++ Program is to generate Fibonacci Series upto n terms...
#include <iostream>
using namespace std;
int main()
{
    int limit;
    cout << "Upto how many terms?";
    cin >> limit;
    int A[limit];
    A[0] = 0;
    A[1] = 1;
    for (int i = 2; i < limit; i++)
    {
        A[i] = A[i - 1] + A[i - 2];
    }
    cout << "Fibonacci Series upto " << limit << " are:";
    for (int i = 0; i < limit; i++)
    {
        cout << A[i] << endl;
    }
    return 0;
}