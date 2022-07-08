//? The objective of this C++ Program is to implement Insertion Sort in unsorted array!
#include <iostream>
using namespace std;
int main()
{
    int i, j, l, key = 1, A[50], temp = 0;
    cout << "Enter how many elements:" << endl;
    cin >> l;
    int len = l;
    for (i = 0; i < l; i++)
    {
        cout << "Enter element:" << endl;
        cin >> A[i];
    }
    i = 1;
    while (l != 1)
    {
        key = A[i];
        j = i - 1;
        while (j >= 0 && A[j] > key)
        {
            A[j + 1] = A[j];
            j -= 1;
        }

        A[j + 1] = key;
        i++;
        l--;
    }

    cout << "Your Sorted Array:" << endl;
    for (i = 0; i < len; i++)
    {
        cout << A[i] << endl;
    }
}