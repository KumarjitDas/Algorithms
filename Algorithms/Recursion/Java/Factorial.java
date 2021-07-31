/**
 * A program to print the factorial of a number in the standard out using
 * recursion.
 * @author Kumarjit Das
 */

/**
 * Main program class.
 */
public class Factorial {
   /**
    * Return the factorial of the value.
    * @param value an integer
    * @return the factorial of the value
    */
   private static int factorial(int value) {
      if (value == 1) return 1;
      return value * factorial(value - 1);
   }

   /**
    * Main entry point of this program.
    * @param args command-line arguments
    */
   public static void main(String args[]) {
      int value = 10;
      System.out.print("Factorial of " + value + ": " + factorial(value));
   }
}
