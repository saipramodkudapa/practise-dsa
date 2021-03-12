

class MinHeap:

    def __init__(self):
        self.heap = []

    def print_heap(self):
        print(self.heap)

    @staticmethod
    def parent_index(index):
        return (index-1)//2

    @staticmethod
    def left_child_index(index):
        return 2*index + 1

    @staticmethod
    def right_child_index(index):
        return 2*index+2

    def has_parent(self, index):
        return self.parent_index(index) >= 0

    def has_left_child(self, index):
        return self.left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        return self.right_child_index(index) < len(self.heap)

    def right_child(self, index):
        return self.heap[self.right_child_index(index)]

    def left_child(self, index):
        return self.heap[self.left_child_index(index)]

    def parent(self, index):
        return self.heap[self.parent_index(index)]

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def add_element(self, element):
        self.heap.append(element)
        self.heapify_up()

    def peek(self):
        if len(self.heap) == 0:
            print('Invalid')
        return self.heap[0]

    def poll(self):
        if len(self.heap) == 0:
            print('Invalid')
        item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()
        return item

    def heapify_up(self):
        current_idx = len(self.heap) - 1
        while self.has_parent(current_idx) and self.parent(current_idx) > self.heap[current_idx]:
            parent_idx = self.parent_index(current_idx)
            self.swap(parent_idx, current_idx)
            current_idx = parent_idx

    def heapify_down(self):
        current_idx = 0

        while self.has_left_child(current_idx):

            smaller_idx = self.left_child_index(current_idx)
            if self.has_right_child(current_idx) and self.right_child(current_idx) < self.left_child(current_idx):
                smaller_idx = self.right_child_index(current_idx)

            if self.heap[smaller_idx] < self.heap[current_idx]:
                self.swap(current_idx, smaller_idx)
            else:
                break

            current_idx = smaller_idx

        return None


if __name__ == '__main__':
    heap = MinHeap()
    heap.add_element(2)
    heap.add_element(1)
    heap.add_element(3)
    heap.add_element(0)
    heap.add_element(-1)
    heap.print_heap()
    print(heap.poll())
    heap.print_heap()
    print(heap.poll())
    heap.print_heap()
    print(heap.poll())
    heap.print_heap()