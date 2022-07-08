//? The objective of this C++ program is to implement bubble sort on an unsorted array!
#include <iostream>
using namespace std;
int main()
{
    int A[50], i, j, k, temp = 0, l;
    cout << "Enter how many elements:" << endl;
    cin >> l;
    for (i = 0; i < l; i++)
    {
        cout << "Enter element:" << endl;
        cin >> A[i];
    }
    cout << "Your Unsorted Array is:" << endl;
    for (i = 0; i < l; i++)
        cout << A[i] << endl;
    for (i = 0; i < l; i++)
    {
        for (j = 0, k = 1; j < l - 1, k < l; j++, k++)
        {
            if (A[j] >= A[k])
            {
                temp = A[j];
                A[j] = A[k];
                A[k] = temp;
            }
        }
    }
    cout << "Your Sorted Array is:" << endl;
    for (i = 0; i < l; i++)
        cout << A[i] << endl;
}