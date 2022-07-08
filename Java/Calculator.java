
//? The objective of this JAVA program is to make a calculator that can perfrom arithmetic operations.
import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1;
        int num2;
        int result;
        char op;
        char c = 'y';
        while (c == 'y') {
            result = 0;
            System.out.println("Enter First Number:");
            num1 = sc.nextInt();
            System.out.println("Enter Second Number:");
            num2 = sc.nextInt();
            System.out.println("Enter operator(+,-,*,/):");
            op = sc.next().charAt(0);
            if (op == '+') {
                result = num1 + num2;
            } else if (op == '-') {
                result = num1 - num2;
            } else if (op == '*') {
                result = num1 * num2;
            } else if (op == '/') {
                result = num1 / num2;
            }
            System.out.println("The Result is:" + result);
            System.out.println("Would you like to try again(y/n):");
            c = sc.next().charAt(0);
        }
        sc.close();
    }

}
