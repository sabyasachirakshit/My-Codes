using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hello
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //This is important for debugging. Do not remove this.

            int mynumber = 19; // takes 4 bytes
            float FloatingNumber = 1.96f;  // takes 4 bytes
            char MyCharacter = 'S'; // takes 2 bytes
            string myString = "SR"; // takes 2 bytes per character
            bool MyBoolean = true;  // takes 1 bit
            Console.WriteLine("Hello World!");
            Console.Write("Hello Sabyasachi");
            Console.WriteLine("I love C# and my roll number is: "+mynumber);
            Console.WriteLine("Testing my declared variables :- Float = "+FloatingNumber+" character= "+MyCharacter+" String= "+myString+" Bool = "+MyBoolean);
            long newLongNumber = 12345678; //takes 8 bytes and is better in precision than int
            double newDouble = 2345.241145; //takes 8 bytes and is better in precision than float
            Console.WriteLine("Long = " + newLongNumber + " Double= " + newDouble);
            // Testing Input
            //Console.WriteLine("Please enter a string:");
            //string inp = Console.ReadLine();
            //Console.WriteLine("Your input was: " + inp);
            // Type Casting 2 types - 1. Implicit [char > int > long > float > double] 2. Explicit
            int x = (int) 3.5; //converting double to integer with type casting
            Console.WriteLine(x);
            int xx = 5;
            double y = xx; // promoting int to double through implicit type casting
            Console.WriteLine(y);
            char xxx = 'a';
            double yy = xxx;
            Console.WriteLine(yy);

            // Operators
            // 1. Arithmetic Operators
            int a = 2, b = 3;
            Console.WriteLine(a + b);
            Console.WriteLine(a - b);
            Console.WriteLine(a * b);
            Console.WriteLine(a / b);

            // 2. Logical Operators
            Console.WriteLine(false && true);
            Console.WriteLine(true && false);
            Console.WriteLine(false && false);
            Console.WriteLine(true && true);

            Console.WriteLine(false || true);
            Console.WriteLine(true || false);
            Console.WriteLine(false || false);
            Console.WriteLine(true || true);

            Console.WriteLine(!false);
            Console.WriteLine(!true);

            // 3. Comparison Operator
            Console.WriteLine(10 > 5);
            Console.WriteLine(10 < 5);
            Console.WriteLine(10 == 5);
            Console.WriteLine(6 <= 6);

            // 4. Assignment Operator
            int n1 = 12;
            int n2 = 5;
            n2 += n1;
            n2 -= 10;
            n1 *= 100;
            n1 /= n2;
            Console.WriteLine(n2);
            Console.WriteLine(n1);

            // using Math function
            int num = Math.Max(12, 123);
            num = (int) Math.Sqrt(36);
            Console.WriteLine(num);

            // using String methods
            string MS = "hello world!";
            Console.WriteLine(MS.Length);
            Console.WriteLine(MS.ToUpper());
            Console.WriteLine(MS[7]);
            Console.WriteLine(MS.IndexOf("world"));
            Console.WriteLine(MS.Substring(4));
            Console.WriteLine(string.Concat(MS, " I am C#"));
            string name = "SR";
            int age = 25;
            Console.WriteLine($"My name is {name}. My age is {age}");
            // If else conditional statements
            if (age >= 21)
            {
                Console.WriteLine("You are eligible for marriage now!");
            }
            else if(age>=18 && age <= 20)
            {
                Console.WriteLine($"You are adult, but you cannot marry ryt now! Please wait {21 - age} year(s)");
            }
            else if(age>10 && age<18)
            {
                Console.WriteLine($"You have {18 - age} years left to become an adult!");
            }
            else
            {
                Console.WriteLine("You are still a child ryt now!");
            }
            Console.ReadLine();
            // let's try making a calculator

            //string usernumber1, usernumber2, userop;
            //int u1, u2;
            //char uop;
            //Console.WriteLine("Enter 1st number:");
            //usernumber1 = Console.ReadLine();
            //u1 = Convert.ToInt32(usernumber1);

            //Console.WriteLine("Enter 2nd number:");
            //usernumber2 = Console.ReadLine();
            //u2 = Convert.ToInt32(usernumber2);

            //Console.WriteLine("Please enter operator (+,-,*,/): ");
            //userop = Console.ReadLine();
            //uop = Convert.ToChar(userop);

            //if (uop == '+')
            //{
            //    Console.WriteLine("Result: " + (u1 + u2));
            //}else if (uop == '-')
            //{
            //    Console.WriteLine("Result: " + (u1 - u2));
            //}
            //else if (uop == '*')
            //{
            //    Console.WriteLine("Result: " + (u1 * u2));
            //}
            //else if (uop == '/')
            //{
            //    Console.WriteLine("Result: " + (u1 / u2));
            //}
            //else
            //{
            //    Console.WriteLine("Wrong Operator");
            //}


}
    }
}
