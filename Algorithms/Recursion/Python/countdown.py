def countdown(value: int):
   """ Print the countdown values.

   countdown
   =========

   The `countdown` function takes an integer value and decreases it. It prints
   the value each time it. It uses 'recursion' to do this.

   Parameters
   ----------

   value: int
      an integer value

   Returns
   -------

   None
   """

   if value <= 0:                                                               # The base case: if the value is zero
      print("Stop!")                                                            # then stop countdown
      return

   print(value, end=' ')
   countdown(value - 1)                                                         # The recursive case: call countdown
                                                                                # (itself) with value decreased by 1

if __name__ == '__main__':
   print('Countdown start:', end=' ')
   countdown(10)
