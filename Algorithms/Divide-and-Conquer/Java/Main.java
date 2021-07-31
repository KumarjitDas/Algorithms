/**
 * A program to print the sum of all the numbers in an array in standard out
 * using divide and conquer.
 * @author Kumarjit Das
 */

import java.util.Random;

/**
 * Main program class.
 */
public class Main {

   private static long get_array_sum(int array[], int index) {
      if (index == array.length) return 0;
      return array[index] + get_array_sum(array, index + 1);
   }

   private static long array_sum(int array[]) {
      return get_array_sum(array, 0);
   }

   /**
    * Create an integer array with random values in the given range.
    * @param count length of the array
    * @param range range of values of each element
    * @return an integer array with random values
    */
   private static int[] get_array_with_random_values(int count, int range) {
      int array[] = new int[count];
      long current_time = System.currentTimeMillis();
      Random random_number_generator = new Random(current_time);
      for (int i = 0; i < array.length; i++) {
         array[i] = (int)(random_number_generator.nextDouble() * range);
      }
      return array;
   }

   /**
    * Print the array in the standard out file
    * @param array an integer array
    */
   private static void print_array(int array[]) {
      for (int value: array) {
         System.out.print(value + ", ");
      }
   }

   /**
    * Main entry point of this program.
    * @param args command-line arguments
    */
   public static void main(String args[]) {
      int array[] = get_array_with_random_values(10, 100);
      System.out.print("Array: ");
      print_array(array);
      System.out.println("\nSum: " + array_sum(array));
   }
}
