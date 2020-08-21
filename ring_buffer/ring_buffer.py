class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * capacity

    def append(self, item):
        if self.size == self.capacity:
            self.storage.append(item)
            self.size += 1

        else:
            self.storage[self.size] = item
            self.size = (self.size + 1) % self.capacity


    def get(self):
        return self.storage
