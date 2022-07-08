
//? The objective of this JAVA program is to generate armstrong numbers in a given range.
import java.util.Scanner;

public class ArmstrongNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start;
        int end;
        System.out.println("Generate Armstrong Numbers in a range!\n");
        System.out.println("Enter start of range:");
        start = sc.nextInt();
        System.out.println("Enter end of range:");
        end = sc.nextInt();
        System.out.println("The Armstrong Numbers between" + start + " and " + end + " are: ");
        while (start <= end) {
            int temp = 0;
            int dig = 0;
            int sum = 0;
            temp = start;
            while (temp > 0) {
                dig = temp % 10;
                sum += dig * dig * dig;
                temp /= 10;
            }
            if (sum == start) {
                System.out.println(start);
            }
            start++;
        }
        sc.close();

    }
}
