'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
  0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''
#the solution

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def countunivalsubtree(node) :
    if node != None :
        if node.left == None and node.right == None :
            return 1
        elif node.left == None :
            if node.right.data == node.data :
                return 1 + countunivalsubtree(node.right)
            return countunivalsubtree(node.right)

        elif node.right == None :
            if node.left.data == node.data :
                return 1 + countunivalsubtree(node.left)
            return countunivalsubtree(node.left)
        else :
            if node.left.data == node.data and node.right.data == node.data :
                return 1 + countunivalsubtree(node.left) + countunivalsubtree(node.right)
            else :
                return  countunivalsubtree(node.left) + countunivalsubtree(node.right)
    else :
        return 0
                


node = Node(0, Node(1), Node(0,Node(1,Node(1),Node(1)),Node(0)))
print(countunivalsubtree(node))
node = Node(1, Node(1,Node(1),Node(1)),Node(1,right=Node(1)))
print(countunivalsubtree(node))