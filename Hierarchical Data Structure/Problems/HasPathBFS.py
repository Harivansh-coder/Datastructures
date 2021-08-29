"""
BFS approch to solve has path problem(if there is a path from source node to destination node).
"""
    
    
def bfs(graph, src, des):
    """
    src = source node
    des = destination node
    following function returns True if there is a path from src-node to des-node else return False
    """

    if (src == des): return True

    queue = [src]

    while (len(queue) != 0):
        current = queue.pop(0)
        if (current == des): return True

        for i in graph[current]:
            queue.append(i)
    
    return False




if __name__ == "__main__":

    graph = {
        'a' : ['b','c'],
        'b' : ['d'],
        'c' : ['e'],
        'd' : ['f','g'],
        'e' : [],
        'f' : [],
        'g' : [],
        'h' : ['f']
    }

    #Testing
    print(bfs(graph, 'a', 'e')) # Yes
    print(bfs(graph, 'a', 'h')) # No
    print(bfs(graph, 'a', 'c')) # Yes


"""
# Output

    True
    False
    True
    
"""


