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
      Index of the 'item' is in the array.
   error_code: int
      The given 'item' is not in the array.
      `error_code` is always -1.
   """

   low = 0
   high = len(array) - 1

   while low <= high:
      # Each time we check for the middle element
      index = (low + high) // 2                                               # `index` is rounded down by Python
                                                                              # automatically if (low + high) isn’t
                                                                              # an even number
      value = array[index]

      if item == value:                                                       # the item is found
         return index

      if item > value:                                                        # the guessed value was too low
         low = index + 1
      else:                                                                   # the guessed value was too high
         high = index - 1

   return -1                                                                  # the item doesn't exist in the array


if __name__ == '__main__':
   # creating an array of values from -10 to +10
   array = [i for i in range(-10, 11)]
   print("Array:", array)

   print("`{}` is at index: {}".format(3, binary_search(array, 3)))
   print("`{}` is at index: {}".format(19, binary_search(array, 19)))
   print("`{}` is at index: {}".format(-7, binary_search(array, -7)))
   print("`{}` is at index: {}".format(-24, binary_search(array, -24)))
