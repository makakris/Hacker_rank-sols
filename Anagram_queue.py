class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
          self.queue.insert(0,dataval)
# Pop method to remove element
  def removefromq(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")
  def revq(self):
      return "".join(self.queue)


TheQueue = Queue()
s1= "pop"
s2="psp"
for i in s1:
    TheQueue.addtoq(i)
if s2==TheQueue.revq():
    print("Anagram")
else:
    print("Not Anagram")