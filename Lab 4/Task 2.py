space_routes = {
    'earth': {'moon_base': 10, 'orbital_platform': 5},
    'orbital_platform': {'moon_base': 2, 'mars': 60},
    'moon_base': {'mars': 50},
    'mars': {}
}

def reconstruct_path(parent_map, destination):
    route = []
    node = destination
    while node is not None:
        route.append(node)
        node = parent_map[node]
    return route[::-1]

def uniform_cost_search(network, source, target):
    frontier = [(source, 0)] 
    explored = set()
    cost_record = {source: 0}
    parent = {source: None}

    while frontier:
        current_node, current_cost = min(frontier, key=lambda x: x[1])
        frontier.remove((current_node, current_cost))

        if current_node in explored:
            continue

        explored.add(current_node)

        if current_node == target:
            optimal_path = reconstruct_path(parent, target)
            print("Optimal route to mars:", optimal_path)
            print("Total fuel required:", current_cost)
            return

        for next_node, fuel_cost in network[current_node].items():
            updated_cost = current_cost + fuel_cost

            if next_node not in cost_record or updated_cost < cost_record[next_node]:
                cost_record[next_node] = updated_cost
                parent[next_node] = current_node
                frontier.append((next_node, updated_cost))

    print("Destination not reachable.")

uniform_cost_search(space_routes, 'earth', 'mars')
