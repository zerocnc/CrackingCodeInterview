class MinStack():
     def __init__(self):
          self.top, self._min = None, None
          return
     def min(self):
          if not self._min:
               return None
          return self._min.data
     def push(self, item):
          if self._min and (self._min.data < item):
               self._min = Node( data = self._min.data, next=self._min)
          else:
               self._min = Node(data=item, next=self.min)
          self.top = Node(data=item, next=self.top)
     def pop(self):
          if not self.top:
               return None
          self._min = self._min.next
          item = self.top.data
          self.top = self.top.next
          return item
class Node():
     def __init__(self, data=None, next = None):
          self.data, self.next = data, next

     def __str__(self):
          string = str(self.data)
          if self.next:
               string += ',' + str(self.next)
          return string

import unittest

class Test(unittest.TestCase):
     def test_min_stack(self):
          min_stack = MinStack()
          #self.assertEqual(min_stack.min(), None)
          print(min_stack.min())
          min_stack.push(7)
          #self.assertEqual(min_stack.min(), 7)
          print("Min:")
          print(min_stack.min())
          print("Push 6")
          min_stack.push(6)
          print("Push 5")
          min_stack.push(5)
          print("Min")
          print(min_stack.min())
          #self.assertEqual(min_stack.min(), 5)
          print("Push 10")
          min_stack.push(10)
          print("Min:  5")
          print(min_stack.min())
          #self.assertEqual(min_stack.min(), 5)
          #self.assertEqual(min_stack.pop(), 10)
          print("Pop:10")
          print(min_stack.pop())
          
          #self.assertEqual(min_stack.pop(), 5)
          print("Pop: 5")
          print(min_stack.pop())

          #self.assertEqual(min_stack.min(), 6)
          print("Min: 6")
          print(min_stack.min())

          #self.assertEqual(min_stack.pop(), 6)
          print("Pop: 6")
          print(min_stack.pop())

          #self.assertEqual(min_stack.pop(), 7)
          print("Pop: 7")
          print(min_stack.pop())

          #self.assertEqual(min_stack.min(), None)
          print("Pop: None")
          print(min_stack.pop())

if __name__ == "__main__":
  unittest.main()