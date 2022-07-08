//? The objective of this C++ Program is to implement Heap Sort in unsorted array!
#include <iostream>
using namespace std;
void heapify(int A[50], int size, int i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    if (left < size and A[left] > A[largest])
        largest = left;
    if (right < size and A[right] > A[largest])
        largest = right;
    int temp = 0;
    if (largest != i)
    {
        temp = A[i];
        A[i] = A[largest];
        A[largest] = temp;
        heapify(A, size, largest);
    }
}
void Heap_Sort(int A[50], int len)
{
    int i, temp = 0;
    for (i = (len / 2) - 1; i >= 0; i--)
    {
        heapify(A, len, i);
    }
    i = len - 1;
    while (i >= 0)
    {
        temp = A[0];
        A[0] = A[i];
        A[i] = temp;
        heapify(A, i, 0);
        i--;
    }
    cout << "Your sorted array is:" << endl;
    for (i = 0; i < len; i++)
    {
        cout << A[i] << endl;
    }
}
int main()
{
    int A[50], i, j, temp = 0, l;
    cout << "Enter How Many ELements:" << endl;
    cin >> l;
    for (i = 0; i < l; i++)
    {
        cout << "Enter element" << endl;
        cin >> A[i];
    }
    cout << "Your Unsorted Array is:";
    for (i = 0; i < l; i++)
    {
        cout << A[i] << endl;
    }
    Heap_Sort(A, l);
}