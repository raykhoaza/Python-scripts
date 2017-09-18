#Implementation of directed graph data structure
class Graph:
    def __init__(self):
        self.nodes = []
    #Function to reset the state of the visited field for each node
    def reset(self):
        for node in self.nodes:
            node.visited = False

#Node class
class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.children = []

#Depth-first search algorithm to traverse through a graph, with the root node
#of the graph as input
def dfs(root):
    print(root.name)
    root.visited = True
    for node in root.children:
        if node.visited == False:
            dfs(node)

#Breadth-first search algorihtm to traverse through a graph, with the root node
#of the graph as input
def bfs(root):
    q = []
    checked = []
    root.visited = True
    q.append(root)

    while(len(q) != 0):
        r = q.pop(0)
        checked.append(r.name)
        #print(r.name)
        for node in r.children:
            if node.visited == False:
                node.visited = True
                q.append(node)

    return checked
#Function to find if a route exist between 2 nodes, with n1 as the begin node
#and n2 as the ending node, returns true or false
def route(n1, n2):
    list = bfs(n1)
    print (list)
    if n2.name in list:
        return True
    else:
        return False
