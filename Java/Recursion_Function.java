import java.util.Scanner;

public class Recursion_Function {
    static int Calc_Power(int n, int p) {
        if (p != 0) {
            return n * Calc_Power(n, p - 1);
        } else {
            return 1;
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number");
        int number = sc.nextInt();
        System.out.println("Enter its power:");
        int power = sc.nextInt();
        int result = Calc_Power(number, power);
        System.out.println("The result is " + result);
        sc.close();
    }
}
