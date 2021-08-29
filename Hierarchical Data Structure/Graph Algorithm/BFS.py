"""
BFS (breadth first search) is graph transversal algorithm.
"""

# bfs function implementation
def bfs(graph, node):
    queue = [node]

    while (len(queue) != 0):
        current = queue.pop(0)
        print(current, end = " ")

        for i in graph[current]:
            queue.append(i)



if __name__ == "__main__":

    graph = {
        'a' : ['b','c'],
        'b' : ['d'],
        'c' : ['e'],
        'd' : ['f'],
        'e' : [],
        'f' : []
    }

    bfs(graph, 'a')

"""
# Output

    a b c d e f
"""