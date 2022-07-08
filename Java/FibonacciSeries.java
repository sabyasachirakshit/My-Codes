
//? The objective of this JAVA program is to generate fibonacci series upto n terms..
import java.util.Scanner;

public class FibonacciSeries {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int limit = 0;
        System.out.println("Upto how many terms?\n");
        limit = sc.nextInt();
        int[] a = new int[limit];
        a[0] = 0;
        a[1] = 1;
        for (int i = 2; i < limit; i++) {
            a[i] = a[i - 1] + a[i - 2];
        }
        System.out.println("Fibonacci Series upto %d terms is:" + limit);
        for (int i = 0; i < limit; i++) {
            System.out.println(a[i]);
        }
        sc.close();
    }
}
