//? The objective of this C++ Program is to make a calculator that can perform basic arithmetic operations.
#include <iostream>
using namespace std;
int main()
{
    int num1, num2, result;
    char choice, op;
    result = 0;
start:
    system("cls");
    cout << "Enter First Number:";
    cin >> num1;
    cout << "Enter Second Number:";
    cin >> num2;
    cout << "Enter operator(+,-,*,/):";
    cin >> op;
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
    cout << "The Result is:" << result;
    cout << "\nWould you like to try again(y/n):";
    cin >> choice;
    if (choice == 'y' || choice == 'Y')
    {
        goto start;
    }
    return 0;
}
