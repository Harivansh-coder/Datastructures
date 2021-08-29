"""
DFS approch to solve has path problem(if there is a path from source node to destination node).
"""

def dfs(graph, src, des):
    """
    src = source node
    des = destination node
    following function returns True if there is a path from src-node to des-node else return False
    """

    if (src == des): return True

    for i in graph[src]:
        if dfs(graph, i, des):
            return True

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
    print(dfs(graph, 'a', 'f')) # Yes
    print(dfs(graph, 'a', 'g')) # Yes
    print(dfs(graph, 'a', 'h')) # No


"""
# Output

    True
    True
    False
"""


