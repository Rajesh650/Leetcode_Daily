class Heap:
    def __init__(self, array):
        self.heap = array
        self.build_max_heap()

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n // 2, -1, -1):
            self.heapify_down(i, n)

    def heapify_down(self, i, size):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest, size)

    def sort_heap(self):
        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify_down(0, i)

    def print_sorted_array(self):
        print(self.heap)


# Example usage:
array = [10,20,15,12,40,25,18]
heap = Heap(array)
heap.sort_heap()
heap.print_sorted_array()  # Output: [1, 3, 4, 5, 10]
