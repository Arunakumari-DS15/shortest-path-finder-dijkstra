
# Shortest Path Finder using Dijkstra's Algorithm

import heapq

# Graph: location -> neighbouring locations and distances
graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2}
}

def dijkstra(graph, source, destination):
    # Initially, all distances are infinity
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)

        # Ignore outdated entries
        if current_distance > distances[current]:
            continue

        # Stop when the destination is reached
        if current == destination:
            break

        for neighbour, weight in graph[current].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current
                heapq.heappush(
                    priority_queue, (new_distance, neighbour)
                )

    # Check whether the destination is reachable
    if distances[destination] == float("inf"):
        return None, None

    # Reconstruct the shortest path
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path, distances[destination]


# Display available locations
print("Available locations:", ", ".join(graph))

source = input("Enter starting location: ").strip().upper()
destination = input("Enter destination: ").strip().upper()

if source not in graph or destination not in graph:
    print("Invalid location. Please choose A, B, C, D or E.")
else:
    path, distance = dijkstra(graph, source, destination)

    if path is None:
        print("No route is available.")
    else:
        print("Shortest path:", " -> ".join(path))
        print("Total distance:", distance, "km")
