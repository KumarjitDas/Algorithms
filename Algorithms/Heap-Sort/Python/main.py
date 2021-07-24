import random


def get_array_with_random_values(no_of_items: int, xrange: int) -> list:
   """Returns a list of random values"""
   return [random.randint(0, int(random.random() * xrange)) \
           for i in range(no_of_items)]


def heapify(array: list, index: int, maximum: int) -> None:
   """Create the heap and swap elements"""
   largest: int = index
   left: int = index * 2 + 1
   right: int = index * 2 + 2
   if left < maximum and array[left] > array[index]:
      largest = left
   if right < maximum and array[right] > array[largest]:
      largest = right
   if largest != index:
      array[index], array[largest] = array[largest], array[index]
      heapify(array, largest, maximum)


def build_heap(array: list) -> None:
   """Build the heap for the given array"""
   for index in range((len(array) // 2) - 1)[::-1]:                             # *[::-1]: end to begin
      heapify(array, index, len(array))


def heap_sort(array: list) -> None:
   """Sort the given array elements using Heap-Sort algorithm"""
   build_heap(array)
   for index in range(len(array))[::-1]:                                        # *[::-1]: end to begin
      array[0], array[index] = array[index], array[0]
      heapify(array, 0, index)


def main() -> None:
   """Main entry point of this program"""
   array = get_array_with_random_values(20, 1000)
   print("Before sorting:", array)
   heap_sort(array)
   print("After sorting:", array)


if __name__ == "__main__":
   main()
