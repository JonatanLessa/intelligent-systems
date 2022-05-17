#BFS - Algoritmo para Busca em Largura

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s," ")

            for i in self.graph[s]:
                #print(visited[i])
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(1, 4)
g.addEdge(2, 4)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(5, 1)

g.BFS(0)