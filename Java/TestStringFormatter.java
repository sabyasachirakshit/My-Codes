class StringFormatter {  
    public static String reverseString(String str){  
        StringBuilder sb=new StringBuilder(str);  
        sb.reverse();  
        return sb.toString();  
    } 
}
public class TestStringFormatter {  
    public static void main(String[] args) {  
        System.out.println(StringFormatter.reverseString("Java is a programming language."));  
        System.out.println(StringFormatter.reverseString("I love Java Programming."));      
        }  
} 