import java.util.Scanner;
import java.lang.Math;
import java.util.*;
class database{
    public static List<Object> consequences(String event,String option,boolean alive,String relations,String location){
        if(event=="event1_1"){
            if(option=="event1_1_o1"){
                System.out.print("Your cellmate replies 'Peace' with the same cold eyes.");
                alive=true;
            }
            else if(option=="event1_1_o2"){
                System.out.print("Your cellmate stays silent but you can see a danger in his eyes.");
                alive=true;
                relations="hostile";
            }
            else{
                System.out.print("Your cellmate also stays silent!");
                alive=true;
            }
        }
        else if(event=="event1_2"){
            if(option=="event1_2_o1"){
                System.out.print("Your cellmate says, 'Take a free advice, stay calm or you will not make it.'");
                alive=true;
            }
            else if(option=="event1_2_o2"){
                System.out.print("The cop gets angry and knocks you out with his baton!");
                alive=false;
            }
            else{
                System.out.print("Your cellmate punches you more hardly and you get hospitalized!");
                alive=true;
                location="hospital";
                relations="hostile";
            }
        }
        return Arrays.asList(alive,relations,location);
    }
    void database_events(){
        Scanner scan=new Scanner(System.in);
        boolean alive=true;
        String event1_1="You are pushed into the cell, the cellmate watches you in a cold manner.";
        String event1_1_o1="1. Say 'Peace bro!'";
        String event1_1_o2="2. Say 'What are you looking at? You Piece of Trash!'";
        String event1_1_o3="3. Stay Silent";
        String event1_2="The cop pushes you in the cell while saying 'Welcome to Prison hotel', you try to balance yourself.The ugly looking cellmate laughs at you.";
        String event1_2_o1="1. Stay calm and try to control anger!";
        String event1_2_o2="2. Stare at cop coldly.";
        String event1_2_o3="3. Punch your cellmate!";
        String relations="normal";
        String location="prison cell";
        int min=1;
        int max=2;
        int choice;
        int random_result=(int)(Math.random()*(max-min+1)+min);
        //List<Object> parameters=consequences("null","null",alive,relations,location);
        if(random_result==1){
            System.out.print(event1_1);
            System.out.println(event1_1_o1);
            System.out.println(event1_1_o2);
            System.out.println(event1_1_o3);
            System.out.println("Enter choice[1-3]:");
            choice=scan.nextInt();
            if(choice==1){
                List<Object> parameters=consequences("event1_1","event1_1_o1",alive,relations,location);
                System.out.println(parameters);
            }
            else if(choice==2){
                List<Object> parameters=consequences("event1_1","event1_1_o2",alive,relations,location);
                System.out.println(parameters);
            }
            else{
                List<Object> parameters=consequences("event1_1","event1_1_o3",alive,relations,location);
                System.out.println(parameters);
            }
        }
        else{
            System.out.print(event1_2);
            System.out.println(event1_2_o1);
            System.out.println(event1_2_o2);
            System.out.println(event1_2_o3);
            System.out.println("Enter choice[1-3]:");
            choice=scan.nextInt();
            if(choice==1){
                List<Object> parameters=consequences("event1_2","event1_2_o1",alive,relations,location);
                System.out.println(parameters);
            }
            else if(choice==2){
                List<Object> parameters=consequences("event1_2","event1_2_o2",alive,relations,location);
                System.out.println(parameters);
            }
            else{
                List<Object> parameters=consequences("event1_2","event1_2_o3",alive,relations,location);
                System.out.println(parameters);
            }
        }
        scan.close();
    }
    
}
 

class text_prison_escape{
    public static void main(String args[]) {
        System.out.print("Welcome to Text-based Adventure game, Prison Escape!");
        //System.out.println("In this game, you will be imprisoned for a certain amount of time.\nYour task is get released!");
        //int min_year=1;
        //int max_year=5;
        // years_imprisonment=(int)(Math.random()*(max_year-min_year+1)+min_year);
        //System.out.println("You have been sentenced for "+years_imprisonment+" years. Survive at all cost and try to get released.");
        //int month=years_imprisonment*12;
        database d=new database();
        d.database_events();

    }
}