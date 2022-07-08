
//? The objective of this JAVA program is to find dactorial of a number!
import java.util.Scanner;

public class Factorial {
    static long factnum(long n) {
        long fact = 1;
        while (n >= 1) {
            fact *= n;
            n--;
        }
        return fact;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Number:");
        int number = sc.nextInt();
        long result = factnum(number);
        System.out.println("The factorial of " + number + " : " + result);
        sc.close();
    }

}
