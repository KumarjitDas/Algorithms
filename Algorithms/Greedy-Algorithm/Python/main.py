def get_approximation(states_needed: set, stations: dict) -> set:
   """Returns the set of stations which cover the most of the states"""
   final_stations = set()
   while states_needed:
      best_station = None
      states_covered = set()
      for station, states in stations.items():
         covered = states_needed & states
         if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
      states_needed -= states_covered
      final_stations.add(best_station)
   return final_stations

def main() -> None:
   """Main entry point of this program"""
   states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
   stations = {}
   stations["kone"]   = set(["id", "nv", "ut"])
   stations["ktwo"]   = set(["wa", "id", "mt"])
   stations["kthree"] = set(["or", "nv", "ca"])
   stations["kfour"]  = set(["nv", "ut"])
   stations["kfive"]  = set(["ca", "az"])
   print("Graph of stations and states:", stations)
   final_stations = get_approximation(states_needed, stations)
   print("Final stations:", final_stations)

if __name__ == "__main__":
   main()
