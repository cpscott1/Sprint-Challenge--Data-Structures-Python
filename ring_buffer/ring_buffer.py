class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.append(item)
        else:
            self.storage.pop(0)
    def get(self, node):
        return self.node
