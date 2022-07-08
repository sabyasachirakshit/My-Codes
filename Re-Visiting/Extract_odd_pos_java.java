import java.util.Scanner;
public class Extract_odd_pos_java {
    public static void main(String[] args)
    {
        int A[]=new int [100];
        int len;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter size of array: ");
        len=sc.nextInt();
        for(int i=0;i<len;i++){
            System.out.println("Enter element "+(i+1)+" : ");
            A[i]=sc.nextInt();
        }
        for(int i=0;i<len;i++){
            if((i+1)%2!=0){
                System.out.print(A[i]);
            }
        }
        sc.close();
    }
    
}
