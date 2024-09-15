# Breadth First Search

def bfs(graph, start):
    visited = [] 
    queue = [start]  

    while queue:
        vertex = queue.pop(0)  
        if vertex not in visited:
            print(vertex)  
            visited.append(vertex)  
           
            queue.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Breadth-First Search starting from vertex A:")
bfs(graph, 'A')
