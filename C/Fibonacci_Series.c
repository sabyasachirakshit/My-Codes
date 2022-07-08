//?The objective of this C Program is to generate Fibonacci Series upto n terms...
#include <stdio.h>
int main()
{
    int limit;
    printf("Upto how many terms?\n");
    scanf("%d", &limit);
    int A[limit];
    A[0] = 0;
    A[1] = 1;
    for (int i = 2; i < limit; i++)
    {
        A[i] = A[i - 1] + A[i - 2];
    }
    printf("Fibonacci Series upto %d terms is:", limit);
    for (int i = 0; i < limit; i++)
    {
        printf("%d\n", A[i]);
    }
    return 0;
}