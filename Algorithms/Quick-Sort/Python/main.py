from typing import List
import random


def quick_sort(array: List[int]) -> List[int]:
   """ Sort the given array elements.

   quick_sort
   =============

   The `quick_sort` function takes an array and returns a new array with
   sorted elements in ascending order using divide and conquer method.

   Parameters
   ----------

   array: List[int]
      An array/list of integers

   Returns
   -------

   new_array: List[int]
      A sorted array/list
   """

   if len(array) < 2:                                                           # The base case: return the array
      return array                                                              # itself if it is empty or has only one
                                                                                # element

   index = len(array) // 2                                                      # The `index` is rounded down by
                                                                                # Python automatically if `len(array)`
                                                                                # is not an even number
   pivot = array[index]                                                         # Getting the middle element or pivot

   lesser = [i for i in array[:index] if i <= pivot] + \
            [i for i in array[index + 1:] if i <= pivot]                        # Getting every element of the array
                                                                                # less than or equal to the pivot value
   greater = [i for i in array[:index] if i > pivot] + \
             [i for i in array[index + 1:] if i > pivot]                        # Getting every element of the array
                                                                                # greater than the pivot value
   return quick_sort(lesser) + [pivot] + quick_sort(greater)                    # Divide and conquer: call itself with
                                                                                # lesser array, the pivot, and with the
                                                                                # greater array
if __name__ == '__main__':
   array = [random.randint(0, int(random.random() * 100)) for i in range(10)]   # Generating an array of random values
   print("Array:", array)

   sorted_array = quick_sort(array)
   print("Sorted array:", sorted_array)
