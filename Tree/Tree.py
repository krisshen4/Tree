class Tree(object):

   def __init__(self, root):
       self.root = root

   def get_value_root(self):
       if self.root is not None:
           return self.root.value
       else:
           return None

    def print_tree(self, root):
        """
        Print Tree with required structure.
        :param root:
        :return:
        """
        def height(self, node):
           if(node == None):
               return 0;
           else:
               return max(self.height(node.left), self.height(node.right)) + 1

        def width(self, node):
            return 2 ** height -1

        def print_update(self, node, row, left, right):
            if not node:
                return center = left + right // 2

            self.update[row][center] = str(node.value)
            print_update(self, node.left, row + 1, left, center - 1)
            print_update(self, node.right, row + 1, center + 1, right)





class Node(object):

   def __init__(self, value, left, right):
       self.value = value
       self.left = left
       self.right = right


if __name__ == '__main__':
   a = Node(2, None, None)
   b = Tree(a)

   print(b.get_value_root())

# simple binary tree
# in this implementation, a node is inserted between an existing node and the root
#
#
# class BinaryTree():
#
#     def __init__(self,rootid):
#       self.left = None
#       self.right = None
#       self.rootid = rootid
#
#     def getLeftChild(self):
#         return self.left
#     def getRightChild(self):
#         return self.right
#     def setNodeValue(self,value):
#         self.rootid = value
#     def getNodeValue(self):
#         return self.rootid
#
#     def insertRight(self,newNode):
#         if self.right == None:
#             self.right = BinaryTree(newNode)
#         else:
#             tree = BinaryTree(newNode)
#             tree.right = self.right
#             self.right = tree
#
#     def insertLeft(self,newNode):
#         if self.left == None:
#             self.left = BinaryTree(newNode)
#         else:
#             tree = BinaryTree(newNode)
#             tree.left = self.left
#             self.left = tree
#
#
# def printTree(tree):
#         if tree != None:
#             printTree(tree.getLeftChild())
#             print(tree.getNodeValue())
#             printTree(tree.getRightChild())
#
#
#
# # test tree
#
# def testTree():
#     myTree = BinaryTree("Maud")
#     myTree.insertLeft("Bob")
#     myTree.insertRight("Tony")
#     myTree.insertRight("Steven")
#     printTree(myTree)
#

# class Node:
#
#     def __init__(self, data):
#
#         self.left = None
#         self.right = None
#         self.data = data
#
#     def insert(self, data):
# # Compare the new value with the parent node
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
#
# # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()
#
# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
#
# root.PrintTree()
# #
# class Node:
#     def __init__(self, val):
#         self.l = None
#         self.r = None
#         self.v = val
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def getRoot(self):
#         return self.root
#
#     def add(self, val):
#         if(self.root == None):
#             self.root = Node(val)
#         else:
#             self._add(val, self.root)
#
#     def _add(self, val, node):
#         if(val < node.v):
#             if(node.l != None):
#                 self._add(val, node.l)
#             else:
#                 node.l = Node(val)
#         else:
#             if(node.r != None):
#                 self._add(val, node.r)
#             else:
#                 node.r = Node(val)
#
#     def find(self, val):
#         if(self.root != None):
#             return self._find(val, self.root)
#         else:
#             return None
#
#     def _find(self, val, node):
#         if(val == node.v):
#             return node
#         elif(val < node.v and node.l != None):
#             self._find(val, node.l)
#         elif(val > node.v and node.r != None):
#             self._find(val, node.r)
#
#     def deleteTree(self):
#         # garbage collector will do this for us.
#         self.root = None
#
#     def printTree(self):
#         if(self.root != None):
#             self._printTree(self.root)
#
#     def _printTree(self, node):
#         if(node != None):
#             self._printTree(node.l)
#             print(str(node.v) + ' ')
#             self._printTree(node.r)
#
# #     3
# # 0     4
# #   2      8
# tree = Tree()
# tree.add(3)
# tree.add(4)
# tree.add(0)
# tree.add(8)
# tree.add(2)
# tree.printTree()
# print ((tree.find(3)).v)
# print (tree.find(10))
# tree.deleteTree()
# tree.printTree()

