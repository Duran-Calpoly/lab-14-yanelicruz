from dataclasses import dataclass, field

@dataclass(frozen=True)
class MaxHeap:
    data: list[int] = field(default_factory=list)

def heapify_up(heap: MaxHeap, index: int) -> MaxHeap:
    if index == 0:
        return heap  # Base case: reached the root of the heap
    parent_index = (index - 1) // 2
    heap_data = heap.data
    if heap_data[index] > heap_data[parent_index]:
        new_heap_data = heap_data[:]
        new_heap_data[index], new_heap_data[parent_index] = new_heap_data[parent_index], new_heap_data[index]
        return heapify_up(MaxHeap(new_heap_data), parent_index)
    else:
        return heap  # No swap needed, return the heap as is

def insert(heap: MaxHeap, element: int) -> MaxHeap:
    new_heap_data = heap.data[:] + [element]
    last_index = len(new_heap_data) - 1
    new_heap = heapify_up(MaxHeap(new_heap_data), last_index)
    return new_heap

def heapify_down(heap: MaxHeap, index: int) -> MaxHeap:
    heap_data = heap.data
    current_size = len(heap_data)
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < current_size and heap_data[left] > heap_data[largest]:
        largest = left

    if right < current_size and heap_data[right] > heap_data[largest]:
        largest = right

    if largest != index:
        new_heap_data = heap_data[:]
        new_heap_data[index], new_heap_data[largest] = new_heap_data[largest], new_heap_data[index]
        return heapify_down(MaxHeap(new_heap_data), largest)
    else:
        return heap  # No swap needed, return the heap as is

def extract_max(heap: MaxHeap) -> tuple[MaxHeap, int]:
    if not heap.data:
        raise ValueError("Heap is empty")

    max_element = heap.data[0]
    new_heap_data = heap.data[:]
    last_index = len(new_heap_data) - 1
    new_heap_data[0] = new_heap_data[last_index]
    new_heap_data = new_heap_data[:last_index]
    new_heap = heapify_down(MaxHeap(new_heap_data), 0)
    return new_heap, max_element
