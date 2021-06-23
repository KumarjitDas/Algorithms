from typing import List


def arraysum(array: List[int]) -> int:
   """ Get the sum of all the elements in the array.

   arraysum
   ========

   The `arraysum` function takes an array and returns the sum of all of its
   elements using divide and concuer method.

   Parameters
   ----------

   array: List[int]
      An array/list of integers

   Returns
   -------

   sum: int
      Sum of all the elements in the array
   """

   if len(array) == 0:                                                          # The base case: if the length of the
      return 0                                                                  # array is 0 then stop

   return array.pop() + arraysum(array)                                         # Divide and conquer: divide the array
                                                                                # into first element and rest of the
                                                                                # elements and call itself with them
if __name__ == '__main__':
   print(f"{arraysum([1, 2, 3, 4, 5, 6, 7]) = }")
