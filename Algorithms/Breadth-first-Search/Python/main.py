from typing      import Dict
from collections import deque


ENDING = 'y'                                                                    # The ending character of a name


def breadth_first_search(name: str, graph: Dict) -> bool:
   """ Search the name ending with `ENDING` in the graph.

   breadth_first_search
   ====================

   The `breadth_first_search` function takes a string and a dictionary and it
   prints the name that ends with `ENDING` in that dictionary.

   Parameters
   ----------

   name: str
      A string value where it starts searching
   graph: Dict
      A dictionary of keys as strings and values as lists/arrays of strings

   Returns
   -------

   True
      If the name is found
   False
      If the name is not found
   """

   search_queue = deque()                                                       # Creating a double-ending queue where
   search_queue += graph[name]                                                  # the names to be searched will be
                                                                                # queued
   searched = []                                                                # A list where searched names will be
                                                                                # stored
   while search_queue:                                                          # Loop until the `search_queue` is not
                                                                                # empty
      name = search_queue.popleft()                                             # Dequeue the first name and check if
      if name not in searched:                                                  # has been searched already or not
         if name[-1] == ENDING:                                                 # If the name ends with `ENDING` print
            print(f"{name}'s name ends with '{ENDING}'.")                       # it and return True
            return True
         else:
            search_queue += graph[name]                                         # If the name does not end with
            searched.append(name)                                               # `ENDING` then enqueue its names in
                                                                                # `search_queue` and add it in the
   return False                                                                 # `searched` list


if __name__ == '__main__':
   graph = {}                                                                   # Creating a graph using with python's
   graph['Me']     = ['Alice', 'Bob', 'Claire']                                 # built-in dicrionary data structure
   graph['Bob']    = ['Anuj', 'Peggy']
   graph['Alice']  = ['Peggy']
   graph['Claire'] = ['Thom', 'Jonny']
   graph['Anuj']   = []
   graph['Peggy']  = []
   graph['Thom']   = []
   graph['Jonny']  = []

   if not breadth_first_search('Me', graph):
      print(f"Person with name ending with '{ENDING}' not found.")
