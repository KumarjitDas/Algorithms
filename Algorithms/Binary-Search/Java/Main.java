/**
 * A program to find an item in a sorted array using Binary-Search
 * algorithm.
 * @author Kumarjit Das
 */
public class Main {
   /**
    * Search the item in the array using Binary-Search algorithm.
    * @param array a sorted(ascending order) array
    * @param item an item to be searched in this array
    * @return the index where this item is found in the array, -1 if not found
    */
   static int binary_search(int array[], int item) {
      int low = 0;
      int high = array.length - 1;
      while (low <= high) {
         int index = (low + high) / 2;
         if (item == array[index])
            return index;
         if (item > array[index])
            low = index + 1;
         else
            high = index - 1;
      }
      return -1;
   }

   /**
    * Main entry point of this program.
    * @param args command-line arguments
    */
   public static void main(String args[]) {
      int array[] = new int[20];
      for (int index = 0, value = -10; index < array.length; index++) {
         array[index] = value++;
      }
      System.out.print("Array: ");
      for (int index = 0; index < array.length; index++) {
         System.out.print(array[index] + ", ");
      }
      System.out.println();
      System.out.println("Search 3: " + binary_search(array, 3));
      System.out.println("Search 19: " + binary_search(array, 19));
      System.out.println("Search -7: " + binary_search(array, -7));
      System.out.println("Search -24: " + binary_search(array, -24));
   }
}
