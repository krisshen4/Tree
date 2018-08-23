import unittest

import numpy as np
import numpy.testing as npt

from ... import Tree, Node


class TestSum(unittest.TestCase):

   def setUp(self):
       self.x = 2
       self.y = 15
       self.answer = 17

       node1 = Node(5, None, None)
       node2 = Node(10, None, None)
       node3 = Node(15, None, None)

       node1.left = node2
       node1.right = node3

       self.tree1 = Tree(node1)

       self.answer1 = [["|", "5", "|"],
                       ["10", "|", "15"]]


   def testSum(self):
       assert self.x + self.y == self.answer

   def testSumVector(self):
       a = np.array([1, 2, 3])
       b = np.array([4, 5, 6])
       assert np.all(a + b == np.array([5, 7, 9]))

   def testSumDecimal(self):
       a = np.array([1.5, 2.9887778, 3.1])
       b = np.array([1, 1, 1])
       npt.assert_almost_equal(a + b, np.array([2.5, 3.988777, 4.1]), decimal=4)
