import random


def find_shortest(array: list[int]) -> int:
   """ Find the shortest element in an array.

   find_shortest
   =============

   The `find_shortest` function takes an array and finds the shortest element
   in it.

   Parameters
   ----------

   array: list[int]
      An array/list of integers

   Returns
   -------

   index: int
      Index of the shortest element is in the array
   """
   index = 0                                                                    # Stores the index of the shortestvalue
                                                                                # value
   shortest = array[index]                                                      # Stores the shortest value

   for i in range(len(array)):
      if array[i] < shortest:
         shortest = array[i]
         index = i

   return index


def selection_sort(array: list[int]) -> list:
   """ Sort the given array elements.

   selection_sort
   =============

   The `selection_sort` function takes an array and returns a new array with
   sorted elements in ascending manner.

   Parameters
   ----------

   array: list[int]
      An array/list of integers

   Returns
   -------

   new_array: list[int]
      A sorted array/list
   """
   new_array = []

   for i in range(len(array)):
      shortest_index = find_shortest(array)                                     # Finds the shortest value in the
      new_array.append(array.pop(shortest_index))                               # array, and adds it to the new array

   return new_array


if __name__ == '__main__':
   array = [random.randint(0, int(random.random() * 100)) for i in range(10)]   # Generating an array of random values
   print("Array:", array)

   sorted_array = selection_sort(array)
   print("Sorted array:", sorted_array)
