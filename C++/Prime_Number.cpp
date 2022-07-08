//? The objective of this C++ program is to generate prime numbers in a given range..
#include <iostream>
using namespace std;
int main()
{
    int start, end;
    cout << "Enter start of range:";
    cin >> start;
    cout << "\nEnter end of range:";
    cin >> end;
    cout << "All prime numbers between " << start << " and " << end << " are:";
    while (start <= end)
    {
        if (start == 1)
        {
            start++;
            continue;
        }
        int temp = start, i = 2, flag = 0;
        while (i < temp)
        {
            if (temp % i == 0)
            {
                flag = 1;
                break;
            }
            i++;
        }
        if (flag == 0)
        {
            cout << start << endl;
        }
        start++;
    }
    return 0;
}