class Node:
    def __init__(self,value):
        self.value = value
        self.neighbours = None
        self.parent = None


def bfs(start):

    current = []
    current.append(start)
    parent={s:None}
    print(start.value)
    no = 0
    while current:
        no+= 1
        next = []
        for i in current:
            if i.neighbours is None:
                return
            for j in i.neighbours:
                if j not in parent:
                    parent[j] = i
                    print(j.value)
                    next.append(j)
        current = next

# defining graph structure
s = Node(0)
v1= Node(1)
v2 = Node(2)
v3 = Node(3)
v4 = Node(4)
v5 = Node(5)
v6 = Node(6)
v7 = Node(7)
v8 = Node(8)

s.neighbours = [v1,v3,v8]
v1.neighbours = [s, v7]
v2.neighbours = [v7, v5, v3]
v3.neighbours = [s,v2, v4]
v4.neighbours = [v3, v8]
v5.neighbours = [v2, v6]
v6.neighbours = [v5]
v7.neighbours = [v1, v2]
v8.neighbours = [s,v4]

bfs(s)
