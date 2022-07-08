import java.util.Scanner;

public class LB_Search {
    static void Linear_Search(int Array[], int search, int size) {
        int flag = 0;
        for (int i = 1; i <= size; i++) {
            if (Array[i] == search) {
                System.out.println("Search Element Found");
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            System.out.println("Search Element Not Found");
        }
    }

    static void Binary_Search(int Array[], int search, int size) {
        int mid;
        if (size == 1) {
            if (Array[0] == search) {
                System.out.println("Element Present!!");
                System.exit(0);
            }

            else {
                System.out.println("Element Not Present!!");
                System.exit(0);
            }

        }

        if (size % 2 != 0)
            mid = (size + 1) / 2;
        else
            mid = size / 2;
        if (Array[mid - 1] == search) {
            System.out.println("Element Present!!");
            System.exit(0);
        } else if (Array[mid - 1] < search) {
            int[] Array1 = new int[20];
            for (int i = mid; i < size; i++) {
                Array1[i] = Array[i];
            }
            Binary_Search(Array1, search, size);
        } else if (Array[mid - 1] > search) {
            int[] Array1 = new int[20];
            for (int i = 0; i < mid; i++) {
                Array1[i] = Array[i];
            }
            Binary_Search(Array1, search, size);
        }
    }

    static void Sort_Array(int Array[], int search, int size) {
        for (int i = 0; i < size; i++) {
            for (int j = 1; j < size; j++) {
                if (Array[i] <= Array[j]) {
                    int temp = Array[i];
                    Array[i] = Array[j];
                    Array[j] = temp;
                }
            }
        }
        Binary_Search(Array, search, size);
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int[] Array = new int[20];
        System.out.println("Enter how many elements:");
        int size = sc.nextInt();
        for (int i = 1; i <= size; i++) {
            System.out.println("Enter element " + i + " : ");
            Array[i] = sc.nextInt();
        }
        System.out.println("Enter Search Element-");
        int search = sc.nextInt();
        System.out.println("1.Linear Search\n2.Binary Search\n\nEnter Which Search you want to perform(1-2):");
        int search_ch = sc.nextInt();
        if (search_ch == 1) {
            Linear_Search(Array, search, size);
        } else if (search_ch == 2) {
            Sort_Array(Array, search, size);

        }
        sc.close();
    }
}