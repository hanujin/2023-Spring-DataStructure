# Practice 4. Binary Search Tree
import sys
from collections import deque
BUILD = 'B'
FIND_MIN = 'm'
FIND_MAX = 'M'
SEARCH = 'S'
INORDER = 'N'
PREORDER = 'R'
POSTORDER = 'O'
class TreeNode:
  def __init__(self, k, l = None, r = None): 
    self.key = k
    self.left = l
    self.right = r

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def isEmpty(self):
    if self.root == None:
      return True
    else:
      return False

  def arrayToBST(self, arr, l, r):
    for i in range(len(arr)-1):
      if arr[i] > arr[i+1]:
        return None
      
      if l > r:
        return None
      
      else:
        idx = (l+r)//2
        center = TreeNode(arr[idx])
        center.left = self.arrayToBST(arr, l, idx-1)
        center.right = self.arrayToBST(arr, idx+1, r)
        return center
      
  def findMin(self):
    curr = self.root
    while curr.left is not None:
      curr = curr.left
    return curr

  def findMax(self):
    curr = self.root
    while curr.right is not None:
      curr = curr.right
    return curr

  def _getHeight(self, curr):
    if not curr:
      return 0
    return 1 + max(self._getHeight(curr.left),self._getHeight(curr.right))

  def _printSpaces(self, n, curr):
    for i in range(int(n)):
      print("  ", end="")
    if not curr:
      print(" ", end="")
    else:
      print(str(curr.key), end="")
  
  def printTree(self):
    if not self.root:
      return 
    q = deque()
    q.append(self.root)
    temp = deque()
    cnt = 0
    height = self._getHeight(self.root) - 1
    nMaxNodes = 2**(height + 1) - 1
    while cnt <= height:
      curr = q.popleft()
      if len(temp) == 0:
        self._printSpaces(nMaxNodes / (2**(cnt+1)), curr)
      else:
        self._printSpaces(nMaxNodes / (2**cnt), curr)
      if not curr:
        temp.append(None)
        temp.append(None)
      else:
        temp.append(curr.left)
        temp.append(curr.right)
      if len(q) == 0:
        print("\n")
        q = temp
        temp = deque()
        cnt += 1

  def search(self, query):
    curr = self.root
    while curr != None:
      if curr.key == query:
        return query
      elif curr.key > query:
        curr = curr.left
      else:
        curr = curr.right

  def writeInorder(self, outFile, x):
    if x != None:
      self.writeInorder(outFile, x.left)
      outFile.write(str(x.key) + " ")
      self.writeInorder(outFile, x.right)

  def writePreorder(self, outFile, x):
    if x != None:
      outFile.write(str(x.key) + " ")
      self.writePreorder(outFile, x.left)
      self.writePreorder(outFile, x.right)

  def writePostorder(self, outFile, x):
    if x != None:
      self.writePostorder(outFile, x.left)
      self.writePostorder(outFile, x.right)
      outFile.write(str(x.key) + " ")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  tree = BinarySearchTree()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == BUILD:
        data = [int(s) for s in words[1:]]
        tree.root = tree.arrayToBST(data, 0, len(data) - 1)
        if tree.root:
          outFile.write(BUILD + "\n")
          tree.printTree()
        else:
          raise Exception("BUILD: invalid input")
      elif op == FIND_MIN:
        found = tree.findMin()
        if not found:
          raise Exception("FindMin failed")
        else:
          outFile.write(str(found.key) + "\n")
      elif op == FIND_MAX:
        found = tree.findMax()
        if not found:
          raise Exception("FindMax failed")
        else:
          outFile.write(str(found.key) + "\n")
      elif op == SEARCH:
        if len(words) != 2:
          raise Exception("SEARCH: invalid input")
        k = int(words[1])
        tree.search(k)
      elif op == INORDER:
        tree.writeInorder(outFile, tree.root)
        outFile.write("\n")
      elif op == PREORDER:
        tree.writePreorder(outFile, tree.root)
        outFile.write("\n")
      elif op == POSTORDER:
        tree.writePostorder(outFile, tree.root)
        outFile.write("\n")
      else:
        raise Exception("Undefined operator")
        
