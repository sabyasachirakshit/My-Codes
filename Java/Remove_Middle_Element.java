import java.util.Scanner;
public class Remove_Middle_Element {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter size of array [size should be odd and greater than 1 and less than 50]: ");
        int size;
        size=sc.nextInt();
        if(size%2==0){
            System.out.println("Unable to catch middle element of even size, try again!");
        }
        else{
            int i=0;
            int j=0;
            int A[]=new int[1000];
            for(i=0;i<size;i++)
            {
                System.out.println("Enter element "+i+" : ");
                A[i]=sc.nextInt();
            }
            int middle_element;
            middle_element=(size+1)/2;
            int[] copy=new int[size-1];
            for(i=0,j=0;i<size;i++){
                if(i!=middle_element-1){
                    copy[j++]=A[i];
                }
            }
            System.out.println("New Array after dropping the middle element is: ");
            for(i=0;i<copy.length;i++){
                System.out.println(copy[i]);
            }

        }
        
    }
}
