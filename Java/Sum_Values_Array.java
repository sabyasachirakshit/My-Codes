import java.util.Scanner;

class Sum_Values_Array

{
    public static void main(String[] args)
    {
        var sc=new Scanner(System.in);
        System.out.println("Enter size of Array:");
        int size;
        int A[]=new int[20];
        size=sc.nextInt();
        for(var i=1;i<=size;i++)
        {
            System.out.println("Enter Element "+i+": ");
            A[i]=sc.nextInt();
        }
        System.out.println("The Array that you have entered is:");
        for(var i=0;i<size;i++)
        {
            System.out.println(A[i]+"\n");
        }
        sc.close();
    }
}