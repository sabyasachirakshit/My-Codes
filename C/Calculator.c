//? The objective of this C Program is to make a calculator that can perform basic arithmetic operations.
#include <stdio.h>
#include <conio.h>
int main()
{
    int num1, num2, result;
    char choice, op;
    result = 0;
start:
    system("cls");
    printf("Enter First Number:");
    scanf("%d", &num1);
    printf("Enter Second Number:");
    scanf("%d", &num2);
    printf("Enter operator(+,-,*,/):");
    scanf(" %c", &op);
    if (op == '+')
    {
        result = num1 + num2;
    }
    else if (op == '-')
    {
        result = num1 - num2;
    }
    else if (op == '*')
    {
        result = num1 * num2;
    }
    else if (op == '/')
    {
        result = num1 / num2;
    }
    printf("The Result is:%d", result);
    printf("\nWould you like to try again(y/n):");
    scanf(" %c", &choice);
    if (choice == 'y' || choice == 'Y')
    {
        goto start;
    }
    return 0;
}