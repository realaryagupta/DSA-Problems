class Queue:
    def __init__(self,size):
        self.size = size
        # making an array with all 0 entries
        self.queue = [0] * size
        self.front = self.rear = -1