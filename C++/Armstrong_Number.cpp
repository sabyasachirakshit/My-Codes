//? The objective of this C++ Program is to generate armstrong numbers in a desired range!
#include <iostream>
using namespace std;
int main()
{
    int start, end;
    cout << "Generate Armstrong Numbers in a range!\n";
    cout << "Enter start of range:";
    cin >> start;
    cout << "Enter end of range:";
    cin >> end;
    cout << "The Armstrong Numbers between" << start << " and " << end << " are:";
    while (start <= end)
    {
        int temp = 0, dig = 0, sum = 0;
        temp = start;
        while (temp > 0)
        {
            dig = temp % 10;
            sum += dig * dig * dig;
            temp /= 10;
        }
        if (sum == start)
        {
            cout << start << endl;
        }
        start++;
    }
    return 0;
}
