## README for Lab 14: Heaps

### Overview

In this lab, you are tasked with understanding and modifying a given Max Heap implementation to create a Min Heap. This involves adjusting the logic in the provided heap operations to maintain the Min Heap property, where the smallest element is always at the root of the heap.

### Objectives

- Convert the provided Max Heap code to a Min Heap.
- Ensure all operations (insert, extract, heapify up, and heapify down) reflect the Min Heap properties.
- Pass all provided unit tests in `test_14.py` which are designed to validate your Min Heap implementation.

### Provided Code

You will receive starter code that includes:
- **MaxHeap class**: A Python class representing a Max Heap.
- **Heap operations**: Functions such as `insert()`, `extract()`, `heapify_up()`, and `heapify_down()` designed for a Max Heap.

### Tasks

1. **Modify the MaxHeap Class**:
   - Rename the class to `MinHeap`.
   - Adjust the internal logic to support the Min Heap properties.

2. **Update Heap Operations**:
   - **Insert**: Ensure the new element maintains the Min Heap property as it is added.
   - **Extract**: Correctly remove the root element (the minimum), and reorder the heap to maintain the heap properties.
   - **Heapify Up**: Adjust the function to ensure that a node is moved up the tree if it is less than its parent, thus maintaining the Min Heap condition.
   - **Heapify Down**: Modify this function to move a node down in the tree if it is greater than its children, ensuring the smallest node is always at the root.

3. **Unit Tests**:
   - Run the provided unit tests in `test_14.py` to ensure your Min Heap implementation functions correctly.

### Submission

Once you have completed the modifications and all unit tests pass:
- Commit your changes to your repository.
- Push your final implementation to GitHub Classroom.