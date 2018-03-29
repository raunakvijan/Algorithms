
class Node:
    def __init__(self,value):
        self.value = value
        self.neighbours = None
        self.parent = None

def dfs(start):
    print(start.value)
    for i in start.neighbours:
        if i not in parent:
            parent[i] = start
            dfs(i)

# defining graph structure
s = Node('s')
a= Node('a')
b = Node('b')
c = Node('c')
d = Node('d')



s.neighbours = [a,b,c]
a.neighbours = [s, d]
b.neighbours = [s,d]
c.neighbours = [s,d]
d.neighbours = [a,b,c]

parent = {s: None}
dfs(s)


