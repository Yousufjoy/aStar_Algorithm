

class Node:
    def __init__(self, nodename, parent=None, g=0, h=0):
        self.nodename = nodename
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

def astar_search(adjacency_list, H):
    start_node = Node('S', None, 0, H['S'])
    priority_queue = [start_node]

    while priority_queue:
        priority_queue.sort(key=lambda x: x.f)
        current_node = priority_queue.pop(0)

        if current_node.nodename == 'G':
            break

        for neighbor, edge_cost in adjacency_list[current_node.nodename]:

            new_g = current_node.g + edge_cost
            new_node = Node(neighbor, current_node, new_g, H[neighbor])
            priority_queue.append(new_node)

    # Path Generation
    path = []
    cost = current_node.g
    while current_node.parent is not None:
        path.insert(0, current_node.nodename)
        current_node = current_node.parent

    path.insert(0, 'S')
    return path, cost


adjacency_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('D', 2), ('G', 3)],
    'D': [('G', 2), ('A', 2)],
    'G': [('C', 4)],
}

H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 1,
    'G': 0,
}

optimal_path, total_cost = astar_search(adjacency_list, H)
print("Optimal Path:", optimal_path)
print("Total Cost:", total_cost)