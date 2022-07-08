
//? The objective of this JaVa program is to generate prime numbers in a given range.
import java.util.Scanner;

public class PrimeNumber {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ALl Prime Numbers will be generated in a given range!");
        int start;
        int end;
        System.out.println("Enter start of range:");
        start = sc.nextInt();
        System.out.println("Enter end of range:");
        end = sc.nextInt();
        System.out.println("All Prime Numbers between " + start + " and " + end + " are:-->");
        while (start <= end) {
            if (start == 1) {
                start++;
                continue;
            }
            int temp = start;
            int i = 2;
            int flag = 0;
            while (i < temp) {
                if (temp % i == 0) {
                    flag = 1;
                    break;
                }
                i++;
            }
            if (flag == 0) {
                System.out.println(start);
            }
            start++;
        }
        sc.close();
    }
}
