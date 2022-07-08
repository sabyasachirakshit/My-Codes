import java.util.Scanner;
abstract class parent2{
    int var2=12;
    public abstract int function2();
}

class parent1 extends parent2{
    int x;
    final int v1=101;
    public int function2(){
        System.out.println("Accessing Abstract Class function from sub-class!");
        return var2;
    }

    public parent1(){
        this.x=3;
    }

    static void function(){
        System.out.println("Accessed without object!");
    }

    public int function1(){
        int variable1=1;
        int variable2=2;
        System.out.println("Inside parent1 function: "+variable2);
        return variable1;
    }

    class child_of_parent1{
        String str="String of a class inside a class";
    }
} 

public class oop extends parent1 {
    public static void main(String[] args){
        parent1 object_of_parent1=new parent1();
        parent1.child_of_parent1 object_of_child_of_parent1=object_of_parent1.new child_of_parent1();
        System.out.println(object_of_parent1.x);
        System.out.println(object_of_parent1.function1());
        //object_of_parent1.v1=100;
        System.out.println(object_of_parent1.v1);
        function();
        System.out.println(object_of_parent1.function2());
        System.out.println(object_of_child_of_parent1.str);
    }
}
