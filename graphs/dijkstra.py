import heapq as priority
import math

visited = {}
parent_node = {}

def dijkstra(start,edges):

    def relax(a, b, wt):
        if b in visited:
            return
        if myDict[b] > myDict[a]+wt:
            myDict[b] = myDict[a]+wt
            parent_node[b] = a
            for i in range(len(h)):
                if h[i][1] == b:
                    h[i][0] = myDict[a]+wt

    h=[]
    myDict = {}
    for i in edges:
        myDict[i] = math.inf
    myDict[start] = 0
    parent_node[start] = None
    [priority.heappush(h, [j,i]) for i, j in myDict.items()]
    visited[start]= True
    a = priority.heappop(h)
    while(a):
        value, vertice = a
        for b,wt in edges[vertice].items():
            relax(vertice, b, wt)

        try:
            a = priority.heappop(h)
            visited[a[1]] = True
        except:
            break

    return myDict


def parent(a):
    if a is not None:
        parent(parent_node[a])
        print(a)


def path(a):
    for i,j in a.items():
        print("path of "+str(i))
        print("path length "+str(j))
        parent(i)
        print('\n')





start = 'S'
edges = {'S':{'A':3,'C':2,'F':6},'A':{'D':1,'B':6},
         'B':{'E':1},'C':{'A':2,'D':3},
         'D':{'E':4},'E':{},'F':{'E':2}}

result = dijkstra(start=start,edges=edges)
path(result)
