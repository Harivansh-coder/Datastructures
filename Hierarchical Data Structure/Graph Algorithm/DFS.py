"""
DFS (depth first search) is graph transversal algorithm.
"""

# dfs function implementation
def dfs(graph, node):
    stack = [node]

    while (len(stack) != 0):
        current = stack.pop()
        print(current, end = " ")

        for i in graph[current]:
            stack.append(i)



if __name__ == "__main__":

    graph = {
        'a' : ['b','c'],
        'b' : ['d'],
        'c' : ['e'],
        'd' : ['f'],
        'e' : [],
        'f' : []
    }

    dfs(graph, 'a')

"""
# Output

    a c e b d f 
"""