// Java program to demonstrate return of
// multiple values from a function using
// list Object class.
import java.util.*;

class GfG {
	public static List<Object> getDetails()
	{
		String name = "Geek";
		int age = 35;
		char gender = 'M';

		return Arrays.asList(name, age, gender);
	}

	// Driver code
	public static void main(String[] args)
	{
		List<Object> person = getDetails();
		System.out.println(person);
	}
}
