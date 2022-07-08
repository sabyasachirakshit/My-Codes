//? The objective of this C++ Program is to implement Merge Sort in unsorted array!
#include <iostream>
using namespace std;

void merge(int A[50], int l, int m, int r)
{
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[50], R[50], i;

    for (i = 1; i <= n1; i++)
    {
        L[i] = 0;
    }

    for (i = 1; i <= n2; i++)
    {
        R[i] = 0;
    }
    i = 0;
    while (i < n1)
    {
        L[i] = A[l + i];
        i++;
    }

    int j = 0;
    while (j < n2)
    {
        R[j] = A[m + 1 + j];
        j++;
    }

    i = 0;
    j = 0;
    int k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            A[k] = L[i];
            i++;
        }
        else
        {
            A[k] = R[j];
            j++;
        }

        k++;
    }

    while (i < n1)
    {
        A[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        A[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(int A[50], int l, int r)
{
    if (l >= r)
        return;
    int m = (l + r - 1) / 2;
    merge_sort(A, l, m);
    merge_sort(A, m + 1, r);
    merge(A, l, m, r);
}
int main()
{
    int A[50], i, l;
    cout << "Please enter the size of list:" << endl;
    cin >> l;
    for (i = 0; i < l; i++)
    {
        cout << "Enter Element:" << endl;
        cin >> A[i];
    }

    merge_sort(A, 0, l - 1);
    cout << "Your sorted array is:" << endl;
    for (int i = 0; i < l; i++)
    {
        cout << A[i] << endl;
    }
}
