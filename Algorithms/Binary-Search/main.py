def binary_search(array: list[int], item: int) -> int:
   """ Search an item in an array.

   binary_search
   =============

   The `binary_search` function takes an sorted array and an item. If the item
   is in the array, the function returns its position or index.

   Parameters
   ----------

   array: list[int]
      an array/list of integers
   item: int
      an integer value

   Returns
   -------

   index: int
      Index of the 'item' is in the array
   -1: int
      The given 'item' is not in the array
   """

   low = 0
   high = len(array) - 1

   while low <= high:
      index = (low + high) // 2                                                 # The `index` is rounded down by
                                                                                # Python automatically if (low + high)
                                                                                # isn’t an even number
      value = array[index]                                                      # Each time we check for the middle
                                                                                # element

      if item == value:                                                         # the item is found
         return index

      if item > value:                                                          # the guessed value was too low
         low = index + 1
      else:                                                                     # the guessed value was too high
         high = index - 1

   return -1                                                                    # the item doesn't exist in the array


if __name__ == '__main__':
   array = [i for i in range(-10, 11)]                                          # Generating an array of values from
                                                                                # -10 to +10
   print("Array:", array)

   print(f"{binary_search(array, 3) = }")
   print(f"{binary_search(array, 19) = }")
   print(f"{binary_search(array, -7) = }")
   print(f"{binary_search(array, -24) = }")
