#!/bin/python3

import math
import os
import random
import re
import sys

class Graph:
    def __init__(self,V, cost_library, cost_road):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.cost_library = cost_library
        self.cost_road = cost_road

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def addListEdges(self, edges):
        for edge in edges:
            self.addEdge(edge[0]-1, edge[1]-1)
            #I start at 0, hackerRank start at 1, thats why -1

    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.DFSUtil(temp, i, visited)
        return temp

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

    def cost_library_road(self):
        components = self.connectedComponents()
        total = 0
        if self.cost_library > self.cost_road:
            for component in components:
                if len(component) == 1:
                    total += self.cost_library
                else:
                    total += self.cost_library + self.cost_road*(len(component)-1)
        elif self.cost_library < self.cost_road:
            for component in components:
                if len(component) == 1:
                    total += self.cost_library
                else:
                    total += self.cost_library*len(component)
        return total

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    g = Graph(n, c_lib, c_road)
    g.addListEdges(cities)
    return g.cost_library_road()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
