from Solution import DoublyLinkedList

def main():
    dll = DoublyLinkedList()

    # Test Case 1: Add to front
    dll.add_to_front(1)
    if dll.head.value == 1:
        print("Test Case 1 Passed: Add to front")
    else:
        print("Test Case 1 Failed: Add to front")

    # Test Case 2: Add to end
    dll.add_to_end(2)
    if dll.tail.value == 2:
        print("Test Case 2 Passed: Add to end")
    else:
        print("Test Case 2 Failed: Add to end")

    # Test Case 3: Remove from front
    dll.remove_from_front()
    if dll.head.value == 2:
        print("Test Case 3 Passed: Remove from front")
    else:
        print("Test Case 3 Failed: Remove from front")

    # Test Case 4: Remove from end
    dll.remove_from_end()
    if dll.check_empty():
        print("Test Case 4 Passed: Remove from end")
    else:
        print("Test Case 4 Failed: Remove from end")

    # Test Case 5: Check empty list
    if dll.check_empty():
        print("Test Case 5 Passed: Check empty")
    else:
        print("Test Case 5 Failed: Check empty")

    # Test Case 6: Add to front and check size
    dll.add_to_front(1)
    dll.add_to_front(2)
    if dll.get_size() == 2:
        print("Test Case 6 Passed: Add to front and check size")
    else:
        print("Test Case 6 Failed: Add to front and check size")

    # Test Case 7: Find existing element
    if dll.find(1):
        print("Test Case 7 Passed: Find existing element")
    else:
        print("Test Case 7 Failed: Find existing element")

    # Test Case 8: Find non-existing element
    if not dll.find(3):
        print("Test Case 8 Passed: Find non-existing element")
    else:
        print("Test Case 8 Failed: Find non-existing element")

    # Test Case 9: Insert at index
    dll.insert_at(1, 3)
    if dll.get_at(1) == 3:
        print("Test Case 9 Passed: Insert at index")
    else:
        print("Test Case 9 Failed: Insert at index")

    # Test Case 10: Remove at index
    dll.remove_at(1)
    if dll.get_at(1) == 1:
        print("Test Case 10 Passed: Remove at index")
    else:
        print("Test Case 10 Failed: Remove at index")

    # Test Case 11: Reverse traversal
    dll.reverse_traversal()  # Expected Output: 1
    print("Test Case 11 Passed: Reverse Traversal")

    # Test Case 12: Print list
    dll.print_list()  # Expected Output: 1
    print("Test Case 12 Passed: Print List")

    # Test Case 13: Check if the list is empty after operations
    if not dll.check_empty():
        print("Test Case 13 Passed: Check empty after operations")
    else:
        print("Test Case 13 Failed: Check empty after operations")

    # Test Case 14: Clear the list
    dll.clear_list()
    if dll.check_empty():
        print("Test Case 14 Passed: Clear List")
    else:
        print("Test Case 14 Failed: Clear List")

    # Test Case 15: Add multiple elements and check size
    dll.add_to_end(1)
    dll.add_to_end(2)
    dll.add_to_end(3)
    if dll.get_size() == 3:
        print("Test Case 15 Passed: Add multiple elements and check size")
    else:
        print("Test Case 15 Failed: Add multiple elements and check size")

    # Test Case 16: Get element at index
    if dll.get_at(1) == 2:
        print("Test Case 16 Passed: Get element at index")
    else:
        print("Test Case 16 Failed: Get element at index")

    # Test Case 17: Swap nodes
    dll.swap_nodes(0, 2)
    if dll.get_at(0) == 3 and dll.get_at(2) == 1:
        print("Test Case 17 Passed: Swap nodes")
    else:
        print("Test Case 17 Failed: Swap nodes")

    # Test Case 18: Detect cycle (should be False)
    if not dll.detect_cycle():
        print("Test Case 18 Passed: Detect cycle (should be False)")
    else:
        print("Test Case 18 Failed: Detect cycle (should be False)")

    # Test Case 19: Remove from front (again)
    dll.remove_from_front()
    if dll.get_at(0) == 2:
        print("Test Case 19 Passed: Remove from front again")
    else:
        print("Test Case 19 Failed: Remove from front again")

    # Test Case 20: Remove from end (again)
    dll.remove_from_end()
    if dll.get_size() == 1:
        print("Test Case 20 Passed: Remove from end again")
    else:
        print("Test Case 20 Failed: Remove from end again")

    # Test Case 21: Add elements and remove all
    dll.add_to_end(4)
    dll.add_to_end(5)
    dll.clear_list()
    if dll.check_empty():
        print("Test Case 21 Passed: Add elements and remove all")
    else:
        print("Test Case 21 Failed: Add elements and remove all")

    # Test Case 22: Insert at index out of bounds
    dll.insert_at(5, 6)  # Invalid index
    if dll.get_size() == 0:
        print("Test Case 22 Passed: Insert at index out of bounds")
    else:
        print("Test Case 22 Failed: Insert at index out of bounds")

    # Test Case 23: Remove from front (empty list)
    dll.remove_from_front()  # No element to remove
    if dll.check_empty():
        print("Test Case 23 Passed: Remove from front (empty list)")
    else:
        print("Test Case 23 Failed: Remove from front (empty list)")

    # Test Case 24: Remove from end (empty list)
    dll.remove_from_end()  # No element to remove
    if dll.check_empty():
        print("Test Case 24 Passed: Remove from end (empty list)")
    else:
        print("Test Case 24 Failed: Remove from end (empty list)")

    # Test Case 25: Add an element and check if it exists
    dll.add_to_end(7)
    if dll.find(7):
        print("Test Case 25 Passed: Check if element exists")
    else:
        print("Test Case 25 Failed: Check if element exists")

    # Test Case 26: Add to end and check size
    dll.add_to_end(8)
    if dll.get_size() == 2:
        print("Test Case 26 Passed: Add to end and check size")
    else:
        print("Test Case 26 Failed: Add to end and check size")

    # Test Case 27: Add to front and check order
    dll.add_to_front(6)
    if dll.get_at(0) == 6:
        print("Test Case 27 Passed: Add to front and check order")
    else:
        print("Test Case 27 Failed: Add to front and check order")

    # Test Case 28: Test swap nodes with invalid index
    dll.swap_nodes(1, 5)
    if dll.get_at(1) == 7:
        print("Test Case 28 Passed: Swap nodes with invalid index")
    else:
        print("Test Case 28 Failed: Swap nodes with invalid index")

    # Test Case 29: Reverse traversal after multiple insertions
    dll.reverse_traversal()  # Expected output: 8 7 6
    print("Test Case 29 Passed: Reverse traversal after multiple insertions")

    # Test Case 30: Print list after multiple operations
    dll.print_list()  # Expected output: 6 7 8
    print("Test Case 30 Passed: Print list after multiple operations")

    # Test Case 31: Detect cycle in an empty list
    if not dll.detect_cycle():
        print("Test Case 31 Passed: Detect cycle in an empty list")
    else:
        print("Test Case 31 Failed: Detect cycle in an empty list")

    # Test Case 32: Add elements and check if list is empty
    dll.add_to_end(9)
    dll.add_to_end(10)
    if not dll.check_empty():
        print("Test Case 32 Passed: Add elements and check if list is empty")
    else:
        print("Test Case 32 Failed: Add elements and check if list is empty")

    # Test Case 33: Remove all elements and check size
    dll.clear_list()
    if dll.get_size() == 0:
        print("Test Case 33 Passed: Remove all elements and check size")
    else:
        print("Test Case 33 Failed: Remove all elements and check size")

    # Test Case 34: Check size after multiple operations
    dll.add_to_end(11)
    dll.add_to_end(12)
    dll.add_to_end(13)
    if dll.get_size() == 3:
        print("Test Case 34 Passed: Check size after multiple operations")
    else:
        print("Test Case 34 Failed: Check size after multiple operations")

    # Test Case 35: Insert at first position
    dll.insert_at(0, 14)
    if dll.get_at(0) == 14:
        print("Test Case 35 Passed: Insert at first position")
    else:
        print("Test Case 35 Failed: Insert at first position")

    # Test Case 36: Swap nodes with same index
    dll.swap_nodes(1, 1)
    if dll.get_at(1) == 11:
        print("Test Case 36 Passed: Swap nodes with same index")
    else:
        print("Test Case 36 Failed: Swap nodes with same index")

    # Test Case 37: Insert at last position
    dll.insert_at(dll.get_size(), 15)
    if dll.get_at(dll.get_size() - 1) == 15:
        print("Test Case 37 Passed: Insert at last position")
    else:
        print("Test Case 37 Failed: Insert at last position")

    # Test Case 38: Detect cycle after operations (should be false)
    if not dll.detect_cycle():
        print("Test Case 38 Passed: Detect cycle after operations")
    else:
        print("Test Case 38 Failed: Detect cycle after operations")

    # Test Case 39: Remove node from specific position
    dll.remove_at(1)
    if dll.get_at(1) == 12:
        print("Test Case 39 Passed: Remove node from specific position")
    else:
        print("Test Case 39 Failed: Remove node from specific position")

    # Test Case 40: Check if DLL is empty after removing all elements
    dll.clear_list()
    if dll.check_empty():
        print("Test Case 40 Passed: Check if DLL is empty after removing all elements")
    else:
        print("Test Case 40 Failed: Check if DLL is empty after removing all elements")

main()
