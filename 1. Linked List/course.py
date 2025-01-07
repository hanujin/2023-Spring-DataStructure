import sys
ADD = 'A'
DELETE = 'D'
FIND = 'F'

class Student:
  def __init__(self, i, n, p=None):
    self.id = i
    self.name = n
    self.next = p

class Course:
  def __init__(self, l=[]):
    self.head = None
    self.size = 0

  def __len__(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  def addStudent(self, newID, newName):
    if self.isEmpty():
      self.head = Student(newID, newName)
      self.size += 1
      return True

    if newID < self.head.id:
      temp = self.head
      self.head = Student(newID, newName, temp)
      self.size += 1
      return True
    
    else:
      prev = None
      curr = self.head
      while curr:
        if curr.id == newID:
          return False
        if (not prev or prev.id < newID) and newID < curr.id:
          newNode = Student(newID, newName, curr)
          prev.next = newNode
          self.size += 1
          return True
        prev = curr
        curr = curr.next
      prev.next = Student(newID, newName)
      self.size += 1
      return True

  def deleteStudent(self, queryID):
    if self.isEmpty():
      return False
    
    curr = self.head
    prev = None
    while curr:
      if curr.id == queryID:
        if not prev:
          self.head = curr.next
        else:
          prev.next = curr.next
        self.size -= 1
        return True
      elif curr.id > queryID:
        return False
      prev = curr
      curr = curr.next
    return False

  def find(self, queryID):
    if self.isEmpty():
      return None
    curr = self.head
    while curr:
      if curr.id == queryID:
        return curr
      elif curr.id > queryID:
        return None
      curr = curr.next
    return None

  def write(self, outFile):
    curr = self.head
    while curr:
      outFile.write(str(curr.id) + " " + str(curr.name) + " ")
      curr = curr.next
    outFile.write("\n")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  course = Course()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == ADD:
        if len(words) != 3:
          raise Exception("ADD: invalid input")
        i, n = int(words[1]), words[2]
        if course.addStudent(i, n):
          course.write(outFile)
        else:
          outFile.write("Addition failed\n")
      elif op == DELETE:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        if course.deleteStudent(i):
          course.write(outFile)
        else:
          outFile.write("Deletion failed\n")
      elif op == FIND:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        found = course.find(i)
        if not found:
          outFile.write("Search failed\n")
        else:
          outFile.write(str(found.id) + " " + found.name + "\n")
      else:
        raise Exception("Undefined operator")