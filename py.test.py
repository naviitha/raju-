import time
start = time.time()
class Stack:
 def __init__(self):
   self.items = [] 
 def isEmpty(self):
   return self.items == [] 
 def push(self, item):
   self.items.append(item)
   print(item) 
 def pop(self):
   return self.items.pop()
 def peek(self):
   return self.items[len(self.items) - 1] 
 def size(self):
   return len(self.items)
s=Stack()
print(s.isEmpty()," - because stack is empty")
print("elements are pushed into stack for Operation")
s.push(11)
s.push(12)
s.push(13)
print("Size",s.size())
print("Peek",s.peek())
print("Pop Operation")
print(s.pop())
print(s.pop())
print("Size",s.size())
print((40* '*'))
end=time.time()
print(f"Runtime of the program is {end - start}")
