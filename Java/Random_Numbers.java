import java.util.Random;

public class Random_Numbers {
    public static void main(String args[]) {
        Random r = new Random();
        int upper_bound = 25;
        int int_random = r.nextInt(upper_bound);
        System.out.println("Random integer value from 0 to " + (upper_bound - 1) + " : " + int_random);
    }
}
