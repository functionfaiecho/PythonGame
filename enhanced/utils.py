import heapq

def dijkstra_algorithm(locations, start, end, min_visits):
    """
    Finds the cheapest path from start to end using Dijkstra's Algorithm.

    Args:
        locations (dict): A graph representing locations and travel costs.
        start (str): The starting point, e.g., 'Changi Airport'.
        end (str): The destination, e.g., 'Marina Bay Floating Platform'.
        min_visits (int): Minimum number of locations to visit before reaching the end.

    Returns:
        tuple: The path with the minimum cost and the total cost.
    """
    # Initialise the priority queue (cost, location, path, visits)
    priority_queue = [(0, start, [], 0)]  
    best_path = []
    min_cost = float('inf')

    # Process the queue
    while priority_queue:
        current_cost, current_location, current_path, visits = heapq.heappop(priority_queue)

        # Update the path with the current location
        current_path = current_path + [current_location]

        # Increment visits for non-start/end locations
        if current_location != start and current_location != end:
            visits += 1

        # Check if we're at the end with enough visits
        if current_location == end and visits >= min_visits:
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = current_path
            continue

        # Add unvisited neighbours to the queue
        for next_location, cost in locations[current_location].items():
            if next_location not in current_path:
                heapq.heappush(priority_queue, (current_cost + cost, next_location, current_path, visits))

    # Return the best path and cost
    return best_path, min_cost
