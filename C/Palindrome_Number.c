//? The objective of this C Program is to check if a number is palindrome or not.
#include <string.h>
#include <stdio.h>
int main()
{
    int num, A[20], temp = 0, i = 0, j = 0, flag = 0, c = 0, dig = 0, B[20];
    char str_num;
    printf("Enter a number:");
    scanf("%d", &num);
    temp = num;
    while (temp > 0)
    {
        dig = temp % 10;
        A[i] = dig;
        i += 1;
        c++;
        temp /= 10;
    }
    for (i = c - 1, j = 0; i > 0, j < c; i--, j++)
    {
        B[j] = A[i];
    }
    for (i = 0; i < c; i++)
    {
        if (A[i] != B[i])
        {
            flag = 1;
            break;
        }
    }
    if (flag == 1)
    {
        printf("Not Palindrome!");
    }
    else
    {
        printf("Palindrome!");
    }
}