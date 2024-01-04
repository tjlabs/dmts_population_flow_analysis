class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.new_mac_queue = [None] * capacity
        self.dis_mac_queue = [None] * capacity
        
        self.head = self.tail = self.size = 0
        
        self.mac_set = set()
        self.new_mac_set = set()
        self.disappeared_mac_set = set()
        self.last_updated = None

    def enqueue(self, item: list):
        if self.isFull():
            self.enqueueWithOverwrite(item)
            return True
        self.queue[self.tail] = item[1]
        
        self.new_mac_set = set(item[1]) - self.mac_set
        self.disappeared_mac_set = self.mac_set - set(item[1])
        self.new_mac_queue[self.tail] = self.new_mac_set
        self.dis_mac_queue[self.tail] = self.disappeared_mac_set
        
        self.last_updated = item[0]
        self.mac_set.update(set(item[1]))
        
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        
        return True
    
    def enqueueWithOverwrite(self, item):
        if self.isFull():
            head_mac_c = set(self.queue[self.head]) - self.mac_set
            self.mac_set.difference_update(head_mac_c)

            # Move the head to the next position to overwrite the oldest element
            self.head = (self.head + 1) % self.capacity
            self.size -= 1

        # Proceed with the normal enqueue process
        return self.enqueue(item)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size