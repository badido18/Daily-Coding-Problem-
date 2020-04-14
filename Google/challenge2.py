'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.

For example, given the following Node class

class Node // look donwd

The following test should pass: //look down

'''
#The class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#My Solution
SEP = "/"
def serialize(root):
    if root != None :
        return ( root.val +SEP+ serialize(root.left) +SEP+ serialize(root.right)  )
    else :
        return "None"


def deserialize(s):
    s = s.split("/")
    try :
        root = Node(s[0])
    except IndexError :
        return None
    stack = []
    #this line is not neccessary  
    curr = root
    #because at the end ,the stack wil return the last element whitch is the root
    left = True 
    for i in range(1,len(s)) :
        if left :
            if s[i] != "None" :
                curr.left = Node(s[i])
                stack.append(curr)
                curr = curr.left
            else :
                left = False
        else :
            if s[i] != "None" :
                curr.right = Node(s[i])
                stack.append(curr)
                curr= curr.right
                left = True
            else :
                curr = stack.pop()
                left = False
    return root



#The test of the problem

node = Node('root', Node('left', Node('left.left')), Node('right',Node("right.left")))
assert deserialize(serialize(node)).left.left.val == 'left.left'

#my test 

node = Node('10', Node('4', Node('1')), Node('15',Node("11")))
print(deserialize(serialize(node)).right.left.val)

#my feedback
#this is a great challenge to manipulate trees in python and save them