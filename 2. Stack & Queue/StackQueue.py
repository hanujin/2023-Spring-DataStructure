import sys

class Empty(Exception):
  pass

class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, d):
    self.queue.append(d)
    return True

  def dequeue(self):
    if (len(self.queue) == 0):
      raise Exception
    else:
      del self.queue[0] 

  def front(self):
    if (len(self.queue) == 0):
      raise Exception
    else:
      return self.queue[0]    

  def write(self, outFile):
    queue_len = len(self.queue)
    for i in range(0, (queue_len)):
      outFile.write(str(self.queue[i]) + " ")
    outFile.write("\n")

class StackViaQueues: 
  def __init__(self):
    self.stack = []

  def push(self, d):
    self.stack.append(d)

  def pop(self):
    if (len(self.stack) == 0):
      raise Exception
    else:
      del self.stack[-1]    

  def peek(self):
    if (len(self.stack) == 0):
      raise Exception
    else:
      return self.stack[-1]

  def write(self, outFile):
    stack_len = len(self.stack)
    for i in range(0, stack_len):
      outFile.write(str(self.stack[i]) + " ")
    outFile.write("\n")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  Q = Queue()
  S = StackViaQueues()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == 'E':
        if len(words) != 2:
          raise Exception("ENQUEUE: invalid input")
        if Q.enqueue(words[1]):
          Q.write(outFile)
        else:
          outFile.write("Enqueue failed\n")   
      elif op == 'D':
        if len(words) != 1:
          raise Exception("DEQUEUE: invalid input")
        Q.dequeue()
        Q.write(outFile)
      elif op == 'F':
        if len(words) != 1:
          raise Exception("FRONT: invalid input")
        val = Q.front()
        outFile.write(val + "\n")
      elif op == 'U':
        if len(words) != 2:
          raise Exception("PUSH: invalid input")
        S.push(words[1])
        S.write(outFile)
      elif op == 'O':
        if len(words) != 1:
          raise Exception("POP: invalid input")
        S.pop()
        S.write(outFile)
      elif op == 'T':
        if len(words) != 1:
          raise Exception("TOP: invalid input")
        val = S.peek()
        outFile.write(val + "\n")
      else:
        raise Exception("Undefined operator")

