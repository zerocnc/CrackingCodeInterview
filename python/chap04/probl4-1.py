# 4.1 Route Between Nodes: Given a bidrected graph, design an algorithm to find out whether there is a route between two nodes.

# Bidirected graph - think of a two way street.
#                  - If there is a path between every pair of vertices, it is called a 'connected graph'
#                  - The graph can also have cycles (or not).

import queue

# Adjacency Lists
# - The most common way to represent a grpah is to use lists (data structure). Every vertex (or node) sotres a list of
#   adjacent vertices in an undirected graph, an edge like (a, b) would be stored twice; once in a's adjacent vertices 
#   and once in b's adjacent vertices.

class Graph(): # A simple class definition for a graph node
    def __init__(self):
        self.max_vertices = 6
        self.vertices = [0] * self.max_vertices  # Create the lists to hold nodes next too
        self.count = 0
    def addNode(self, x):
        if self.count < self.max_vertices:
            self.vertices[self.count] = x
            self.count += 1
        else:
            print("Graph full")

    def getNodes(self):
        return self.vertices


class Node():

    def __init__(self, vertex, adjacentLength):
        self.adjacent = [0] * adjacentLength
        self.vertex = vertex
        self.adjacentCount = 0
        self.visited = False

    def addAdjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            print ("No more adjacent nodes can be added")

    def getAdjacent(self):
        return self.adjacent

    def getVertex(self):
        return self.vertex


# BFS is a bit less intiutive, the main tripping point is the (false) assumption that
# BFS is recrusive. It's not. Instead it uses a queue. In BFS, node a vists each of 
# a's neighbors before visiting any of their neighbors. You can think of this as 
# searching level by level out from a. An iterative soultion involving a queue 
# usually works best.
#  Time Complexity,
#       since all the nodes and vertices are visited, the time comlexity for BFS on
#       a graph is O(V+E); where V is the number of vertices and E is the number of
#       edges.
def breadthfirstsearch(g, start, end):
    if start == end:
        return True
    # Create the queue to hold each of the nodes in the graph.
    q = queue.Queue(len(g.getNodes()))
    start.visited = True
    q.put(start)

    # Cycle though the queue buy pumping out each node in the graph.
    while not q.empty():
        r = q.get() # remove an item from the queue.
        if r != None: # checking if not empty; otherwise process item reterived
            adjacent = r.getAdjacent()
            for i in range(len(adjacent)):
                if adjacent[i].visited == False:
                    if adjacent[i] == end:
                        return True
                    else:
                        q.put(adjacent[i])
                    adjacent[i].visited = True
    return False



def createNewGraph():
    g = Graph()
    sizegraph = 6
    temp = [0] * sizegraph

    temp[0] = Node("a", 3)
    temp[1] = Node("b", 0)
    temp[2] = Node("c", 0)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 1)
    temp[5] = Node("f", 0)

    temp[0].addAdjacent(temp[1])
    temp[0].addAdjacent(temp[2])
    temp[0].addAdjacent(temp[3])
    temp[3].addAdjacent(temp[4])
    temp[4].addAdjacent(temp[5])

    for i in range(sizegraph):
        g.addNode(temp[i])
    return g


def createNewGraphWithLoop():
    g = Graph()
    sizegraph = 6
    temp = [0] * sizegraph

    temp[0] = Node("a", 1)
    temp[1] = Node("b", 1)
    temp[2] = Node("c", 1)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 2)
    temp[5] = Node("f", 0)

    temp[0].addAdjacent(temp[1])
    temp[1].addAdjacent(temp[2])
    temp[2].addAdjacent(temp[3])
    temp[3].addAdjacent(temp[4])
    temp[4].addAdjacent(temp[1])
    temp[4].addAdjacent(temp[5])

    for i in range(sizegraph):
        g.addNode(temp[i])
    return g

g = createNewGraphWithLoop()
n = g.getNodes()
start = n[0]
end = n[5]
print ("Start at: " + start.getVertex() + "\nEnd at: " + end.getVertex() )
print ( breadthfirstsearch(g, start, end)) 