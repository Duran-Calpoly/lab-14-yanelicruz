import unittest
from lab14 import MinHeap, insert, heapify_down, extract_min

class TestMinHeap(unittest.TestCase):
    def test_heapify_up(self):
        heap = MinHeap([10, 15, 20, 25])
        heap = insert(heap, 5)
        self.assertEqual(heap.data, [5, 10, 20, 25, 15])

    def test_heapify_down(self):
        # This setup places a larger number at the root and expects a reordering
        heap = MinHeap([36, 19, 1, 17, 3, 25, 2, 2, 7])
        heap = heapify_down(heap, 0)
        # After heapify_down, the root should be one of the smallest elements
        self.assertEqual(heap.data, [1, 19, 2, 17, 3, 25, 36, 2, 7])

    def test_insert(self):
        heap = MinHeap([])
        heap = insert(heap, 5)
        heap = insert(heap, 10)
        heap = insert(heap, 3)
        heap = insert(heap, 1)
        heap = insert(heap, 4)
        self.assertEqual(heap.data, [1, 3, 5, 10, 4])

    def test_extract_min(self):
        heap = MinHeap([1, 3, 5, 10, 4])
        heap, min_element = extract_min(heap)
        self.assertEqual(min_element, 1)
        self.assertEqual(heap.data, [3, 4, 5, 10])

if __name__ == '__main__':
    unittest.main()




