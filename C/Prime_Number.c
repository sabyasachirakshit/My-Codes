//? The objective of this C program is to generate prime numbers in a given range..
#include <stdio.h>
int main()
{
    int start, end;
    printf("Enter start of range:");
    scanf("%d", &start);
    printf("\nEnter end of range:");
    scanf("%d", &end);
    printf("All prime numbers between %d and %d are:", start, end);
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
            printf("\n%d", start);
        }
        start++;
    }
    return 0;
}