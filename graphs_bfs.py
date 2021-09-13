# example 1 (Imran Ahmed)
'''
           Adam
        /    |    \
     Wayne  Nick  Mike 
       |
      Ian
       |
      Fred   
'''
graph = {
    "Adam": {"Wayne", "Nick", "Mike"},
    "Wayne": {"Ian", "Adam"},
    "Ian": {"Wayne", "Fred"},
    "Fred": {"Ian"},
    "Nick": {"Adam"},
    "Mike": {"Adam"},
}

def bfs(graph, start):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            
            for neighbour in neighbours:
                queue.append(neighbour)
                
    return visited

lst = bfs(graph, "Nick")
print(lst)





# example 2

''' 
           A
        /     \
       B       C
     /   \       \ 
    D     E --->  F
'''

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [], 
}

visited = []  # list to keep track of visited nodes
queue = []  # initializes a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s, end="")
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
l = bfs(visited, graph, "A")
print(l)