class Queue:
    def __init__(self, size) -> None:
        self.queue = [None]*size
        self.tail = 0
        self.head = 0
        self.size_ = size
        self.s = 0

    def enqueue(self, element):
        if self.tail == self.head and self.s > 0:
            raise OverflowError
        else:
            self.queue[self.tail] = element

            self.tail += 1
            if self.tail >= self.size_:
                self.tail = 0
            self.s += 1

    def dequeue(self):
        if self.tail == self.head and self.s == 0:
            raise IndexError
        else:
            element = self.queue[self.head]
            self.queue[self.head] = None
            self.head += 1
            if self.head >= self.size_:
                self.head = 0
            self.s -= 1
            return element

    def size(self) -> int:
        return self.s
