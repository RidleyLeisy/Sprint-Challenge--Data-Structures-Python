class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
      
  def append(self, item):
    self.storage[self.current] = item # append item at current location
    self.current += 1 # increment location
    if self.current == self.capacity: # check whether the location is equal to our capacity
      self.current = 0 # if so, change current to 0 and start appending from front


  def get(self):
    if None in self.storage:
      return self.storage[0:self.current]
    else:
      return self.storage

