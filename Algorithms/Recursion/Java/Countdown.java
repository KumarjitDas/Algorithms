/**
 * A program to print the countdown from a number in the standard out using
 * recursion.
 * @author Kumarjit Das
 */

/**
 * Main program class.
 */
public class Countdown {
   /**
    * Countdown to 0 from the starting point and print the counts to standard
    * out.
    * @param count starting point of the countdown
    */
   private static void countdown(int count) {
      if (count == 0) {
         System.out.println("...Stop!");
         return;
      }
      System.out.print(count + " ");
      countdown(count - 1);
   }

   /**
    * Main entry point of this program.
    * @param args command-line arguments
    */
   public static void main(String args[]) {
      System.out.print("Countdown: Start... ");
      countdown(10);
   }
}
