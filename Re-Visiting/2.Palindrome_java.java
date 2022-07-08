import java.util.Scanner;
class Palindrome_java{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int len=1;
        int flag=0;
        System.out.println("Enter String:");
        String str=sc.nextLine();
        System.out.println("String is:"+str);
        char[] ch = str.toCharArray();
        for(int i:ch){
            len++;
        }
        int j=2;
        for (int i=0;i<len-1;i++)
            {
                if(ch[i]==ch[len-j]){
                    flag=0;
                }
                else{
                    flag=1;
                    break;
                }
                j++;
            }
        if(flag==1){
            System.out.println("String "+str+" is not palindrome! ");
        }
        else{
            System.out.println("String "+str+" is palindrome! ");
        }
    }
}