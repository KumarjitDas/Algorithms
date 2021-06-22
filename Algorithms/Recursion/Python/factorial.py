def factorial(value: int) -> int:
   """ Calculates the factorial of the given value.

   factorial
   =========

   The `factorial` function takes an positive integer value and calculates the
   factorial (n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1).

   Parameters
   ----------

   value: int
      an positive integer value

   Returns
   -------

   factorial: int
      factorial of the value (value!)
   """

   if value == 1:                                                               # The base case: if the value is 1 then
      return 1                                                                  # stop recursion and return

   return value * factorial(value - 1)                                          # The recursive case: call the
                                                                                # factorial function with value
                                                                                # decreased by 1
if __name__ == '__main__':
   print(f"{factorial(10) = }")
