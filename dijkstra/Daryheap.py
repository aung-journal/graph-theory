import heapq

class DaryHeap:
    def __init__(self, d):
        self.d = d
        self.heap = []
        self.position = {}

    def push(self, key, value):
        if key in self.position:
            self.decrease_key(key, value)
        else:
            heapq.heappush(self.heap, (value, key))
            self.position[key] = value

    def decrease_key(self, key, value):
        if key in self.position and value < self.position[key]:
            self.remove(key)
            heapq.heappush(self.heap, (value, key))
            self.position[key] = value

    def pop(self):
        value, key = heapq.heappop(self.heap)
        del self.position[key]
        return key, value

    def remove(self, key):
        index = self.heap.index((self.position[key], key))
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        if index < len(self.heap):
            heapq._siftup(self.heap, index)
            heapq._siftdown(self.heap, 0, index)

    def __len__(self):
        return len(self.heap)

    def __contains__(self, key):
        return key in self.position
