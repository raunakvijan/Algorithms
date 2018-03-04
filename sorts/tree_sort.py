class Node:
    right=None
    left=None
    def __init__(self,data):
        self.data=data

class Tree:
    def __init__(self):
        self.root=None



    def add(self,val):
        if self.root==None:
            self.root=Node(val)

        else:
            self._add(self.root,val)

    def _add(self,node,val):
        if(node.data>=val):
            if(node.left==None):
                node.left=Node(val)
            else:
                self._add(node.left,val)
        else:
            if (node.right == None):
                node.right = Node(val)
            else:
                self._add(node.right, val)

    def print_tree(self):
        self.print_treenode(self.root)


    def print_treenode(self,node):
        if(node.left!=None):
            self.print_treenode(node.left)
        print(node.data,end=" ")
        if (node.right != None):
            self.print_treenode(node.right)


    def get_ht(self):
        ht=self.getheight(self.root)
        return ht

    def getheight(self,node):
        if(node.left==None and node.right==None):
            return 0

        if(node.left==None and node.right!=None):
            return self.getheight(node.right)+1

        if (node.left != None and node.right == None):
            return (self.getheight(node.left)+1)

        if (node.left != None and node.right != None):
            return max(self.getheight(node.left),self.getheight(node.right))+1




inp=[5,4,3]
tree=Tree()
for i in inp:
    tree.add(i)
tree.print_tree()

print("\n")
print(tree.get_ht())