class MyCircularQueue:
    
    def __init__(self, k: int):
        
        self.queue = [0] * k
        self.head = -1
        self.tail = -1
        self.max_size = k

    def enQueue(self, value: int) -> bool:
        
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.max_size
        return True

    def Front(self) -> int:
        
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        
        return (self.tail + 1) % self.max_size == self.head

