# Depth First Search 


def dfs(graph, start):
    visited = set()  
    stack = [start]  

    while stack:
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex)  
            visited.add(vertex)  
            
            stack.extend(set(graph[vertex]) - visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting the DFS from node 'A'
print("Depth-First Search starting from vertex A:")
dfs(graph, 'A')
