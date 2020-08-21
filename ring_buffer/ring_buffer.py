class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.size = 0
            self.storage[self.size] = item
            self.size = (self.size + 1) % self.capacity
        else:
            self.storage.append(item)

    def get(self):
        return self.storage
