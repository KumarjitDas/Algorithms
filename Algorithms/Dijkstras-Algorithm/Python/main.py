def find_lowest_cost_node(costs: dict, processed: list) -> dict:
   """Return the node with the lowest cost"""
   lowest_cost = float("inf")                                                   # Infinity
   lowest_cost_node = None
   for node in costs:
      cost = costs[node]
      if cost < lowest_cost and node not in processed:
         lowest_cost = cost
         lowest_cost_node = node
   return lowest_cost_node

def dijstras_algorithm(graph: dict, costs: dict, parents: dict) -> None:
   """Find the fastest path using Dijstra's Algorithm"""
   processed = []
   node = find_lowest_cost_node(costs, processed)
   while node is not None:
      cost: int = costs[node]
      neighbours: dict = graph[node]
      for neighbour in neighbours.keys():
         new_cost = cost + neighbours[neighbour]
         if costs[neighbour] > new_cost:
            costs[neighbour] = new_cost
            parents[neighbour] = node
      processed.append(node)
      node = find_lowest_cost_node(costs, processed)

def print_parent_to_child(parents: dict, start: str, end: str) -> None:
   """Print a graph of parents as `parnet to child` form"""
   parent_to_child: str = end
   node: str = parent_to_child
   while node != start:
      temporary = parents[node]
      parent_to_child = temporary + " -> " + parent_to_child
      node = temporary
   print(parent_to_child)

def main() -> None:
   """Main entry point of this program"""
   infinity = float("inf")
   # Find the fastest path from "Book" to "Piano"
   graph = {
      "Book": { "LP": 5, "Poster": 0 },
      "LP": { "Guiter": 15, "Drums": 20 },
      "Poster": { "Guiter": 30, "Drums": 35 },
      "Guiter": { "Piano": 20 },
      "Drums": { "Piano": 10 },
      "Piano": {}
   }
   costs = { "LP": 5, "Poster": 0, "Guiter": infinity, "Drums": infinity, \
             "Piano": infinity }
   parents = { "LP": "Book", "Poster": "Book", "Piano": None }
   dijstras_algorithm(graph, costs, parents)
   print(f"{graph = }\n{costs = }\n{parents = }\n")
   print("The fastest path is:", end=" ")
   print_parent_to_child(parents, "Book", "Piano")

if __name__ == "__main__":
   main()
