# example 1

''' 
           A
        /     \
       B       C
     /   \       \ 
    D     E --->  F
''' 

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

visited = set()  # sets don't allow repeated elements

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)  # recursion
        return visited
            
l = dfs(visited, graph, 'A')
print(l)
# Time complexity: O(V+E)
# Space complexit: O(V)


# example 2

'''
               A
        /             \
       B               C
    /     \          /   \
   D       E        F     G
  / \     / \      /  \
 H   I   J   K    L    M
'''

default_dict = {
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['A','F', 'G'],
    'D': ['B', 'H', 'I'],
    'E': ['B', 'J', 'K'],
    'F': ['C', 'L', 'M'],
    'G': ['C'],
    'H': ['D'],
    'I': ['D'],
    'J': ['E'],
    'K': ['E'],
    'L': ['F'],
    'M': ['F'],
}

# def dfs(adj)