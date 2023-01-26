import java.util.Scanner;
class String_Reversal_java{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int len=1;
        System.out.println("Enter String:");
        String str=sc.nextLine();
        System.out.println("String is:"+str);
        char[] ch = str.toCharArray();
        for(int i:ch){
            len++;
        }
        System.out.println("Reverse of string "+str+" is: ");
        for (int i=len-1;i!=0;i--) {
            System.out.print(ch[i-1]+"");
        }
    }
}