//? The objective of this C Program is to generate armstrong numbers in a desired range!
#include <stdio.h>
int main()
{
    int start, end;
    printf("Generate Armstrong Numbers in a range!\n");
    printf("Enter start of range:");
    scanf("%d", &start);
    printf("Enter end of range:");
    scanf("%d", &end);
    printf("The Armstrong Numbers between %d and %d are:", start, end);
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
            printf("\n%d", start);
        }
        start++;
    }
    return 0;
}
