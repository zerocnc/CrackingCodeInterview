####################################################################
# Structure: The placement of each element in the binary tree must
#            satisfy the binary search property: the value of the key of
#            an element is greater than the value of the key of the any element
#            element in its left subtree, and less than the value of the
#            key of an elment in its right subtree.
####################################################################

class Node:
     def __init__(self, value = None, leftNode = None, rightNode = None):
          self.value = value
          self.rightNode = rightNode
          self.leftNode = leftNode
     def __str__ (self):
          return str(self.value)

# Operations (provided by TreeADT)
# Assumptions: Before any call is made to a tree operation, the tree has
#              been delcared and a constructor has been applied.
class Tree:
     
     def __init__(self):
          self.root = None

     def insert(self, value):
          self.InsertItem(value, self.root)
          
     def InsertItem(self, value, childRoot):
          if ( self.root is None):
               self.root = Node(value)
          elif value < childRoot.value :
               self.InsertItem(value, childRoot.left)
          else: 
               self.InsertItem( value, childRoot.right)

def main():
     print("Hello!")
     myTree = Tree()

     myTree.insert(1)
     myTree.insert(3)
     myTree.insert(2)
     myTree.insert(5)
     print("End")


     

main()