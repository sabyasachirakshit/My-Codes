
//? The objective of this Java program is to check if a number is palindrome or not.
import java.util.Scanner;

public class PalindromeNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num;
        int[] a = new int[20];
        int temp = 0;
        int i = 0;
        int j = 0;
        int flag = 0;
        int c = 0;
        int dig = 0;
        int[] b = new int[20];
        System.out.println("Enter a number:");
        num = sc.nextInt();
        temp = num;
        while (temp > 0) {
            dig = temp % 10;
            a[i] = dig;
            i += 1;
            c++;
            temp /= 10;
        }
        i = c - 1;
        j = 0;
        while (i >= -1 || j <= c + 1) {
            if (i == -1) {
                break;
            }

            b[j] = a[i];
            i--;
            j++;
        }
        for (i = 0; i < c; i++) {
            if (a[i] != b[i]) {
                flag = 1;
                break;
            }
        }
        if (flag == 1) {
            System.out.println("Not Palindrome!");
        } else {
            System.out.println("Palindrome!");
        }
        sc.close();
    }
}
