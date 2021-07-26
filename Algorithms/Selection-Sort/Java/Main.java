/**
 * A program to sort an array of integers in ascending order using Selection-
 * Sort algorithm.
 * @author Kumarjit Das
 */

import java.util.Random;

/**
 * Selection-Sort class.
 */
class SelectionSort {
   /**
    * Find the smallest element in the array and return its index.
    * @param array an integer array
    * @param begin_index the index from where to start finding
    * @return the index of the smallest element
    */
   private static int find_smallest_index(int array[], int begin_index) {
      int index = begin_index;
      int value = array[index];
      for (int i = begin_index + 1; i < array.length; i++) {
         if (array[i] < value) {
            value = array[i];
            index = i;
         }
      }
      return index;
   }

   /**
    * Swap the array elements of the given indices.
    * @param array an integer array
    * @param index1 a valid index of the array
    * @param index2 a valid index of the array
    */
   private static void swap(int array[], int index1, int index2) {
      int temporary_value = array[index1];
      array[index1] = array[index2];
      array[index2] = temporary_value;
   }

   /**
    * Sort the array using Selection-Sort algorithm.
    * @param array an integer array
    */
   public static void sort(int array[]) {
      for (int i = 0; i < array.length; i++) {
         int shortest_index = find_smallest_index(array, i);
         swap(array, i, shortest_index);
      }
   }
}

/**
 * Main program class.
 */
public class Main {
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
      int array[] = get_array_with_random_values(20, 500);
      System.out.print("\nBefore sorting: ");
      print_array(array);
      SelectionSort.sort(array);
      System.out.print("\nAfter sorting: ");
      print_array(array);
   }
}
