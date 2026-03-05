import heapq
graph = {
    'S' : [('A',2), ('B',5), ('C',4)],
    'A' : [('D',7), ('E',3)],
    'B' : [('F',6)],
    'C' : [('G',2)],
    'D' : [('T',4)],
    'E' : [('T',6)],
    'F' : [('T',5)],
    'G' : [('T',3)],
    'T' : []
}

def beam_search(start, goal, beam_width = 2):
    beam = [(0, [start])]

    while beam:
        candidates = []

        for cost, path in beam:
            current_node = path[-1]

            if current_node == goal:
                return path, cost 

            for neighbour, edge_cost in graph.get(current_node, []):
                new_cost = cost + edge_cost
                new_path = path + [neighbour]
                candidates.append((new_cost, new_path))

        beam = heapq.nsmallest(beam_width, candidates, key = lambda x: x[0])

    return None, float('inf')
    
start = 'S'
goal = 'T'
for k in [1,2,3]:
    path, cost = beam_search(start, goal, k)
    print("Beam width = ", k)
    if path:
        print("Path:","->".join(path))
        print("total cost:", cost)
    else:
        print("path not found")
    print()

