class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.size = 0
        # self.storage = []
        self.queue = [None] * capacity
        self.tail = -1
        self.head = 0
        self.size = 0
    def append(self, item):
        if self.size != self.capacity:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = item
            self.size += 1
    def get(self):
        if self.size is not None:
            index = self.head
            for i in range(self.size):
                print(self.queue[index])
                index = (index + 1) % self.capacity
