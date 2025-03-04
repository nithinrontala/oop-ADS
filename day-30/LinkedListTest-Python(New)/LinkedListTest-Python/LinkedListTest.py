# linked_list_test.py
# This script tests your MyLinkedList implementation.
# It expects a file (for example, my_linked_list.py) containing the MyLinkedList class.
# Ensure that the __str__ method of MyLinkedList prints the list in the following format:
# - For non-empty lists, each element is printed within square brackets (e.g., "[elem1][elem2]")
# - For an empty list, the string "LinkedList is empty" is returned

from Solution import MyLinkedList  # adjust the import according to your implementation

def run_tests():
    linkedlist = MyLinkedList()
    count = 0

    # Test case 1: Add an element to an empty list
    linkedlist.add("Hello")
    if "[Hello]" == linkedlist.to_string():
        print("Test case 1 passed")
        count += 1
    else:
        print("Test case 1 failed")

    # Test case 2: Add multiple elements
    linkedlist.add("World")
    linkedlist.add("!")
    if "[Hello][World][!]" == linkedlist.to_string():
        print("Test case 2 passed")
        count += 1
    else:
        print("Test case 2 failed")

    # Test case 3: Add an element at the beginning
    linkedlist.add_first("First")
    if "[First][Hello][World][!]" == linkedlist.to_string():
        print("Test case 3 passed")
        count += 1
    else:
        print("Test case 3 failed")

    # Test case 4: Check if the list contains an existing element
    if linkedlist.contains("World"):
        print("Test case 4 passed")
        count += 1
    else:
        print("Test case 4 failed")

    # Test case 5: Check if the list contains a non-existing element
    if not linkedlist.contains("NotHere"):
        print("Test case 5 passed")
        count += 1
    else:
        print("Test case 5 failed")

    # Test case 6: Get the first element in the list
    if "First" == linkedlist.get_first():
        print("Test case 6 passed")
        count += 1
    else:
        print("Test case 6 failed")

    # Test case 7: Remove the first element from the list
    linkedlist.remove()
    if "[Hello][World][!]" == linkedlist.to_string():
        print("Test case 7 passed")
        count += 1
    else:
        print("Test case 7 failed")

    # Test case 8: Remove the last element from the list
    linkedlist.remove_last()
    if "[Hello][World]" == linkedlist.to_string():
        print("Test case 8 passed")
        count += 1
    else:
        print("Test case 8 failed")

    # Test case 9: Find the middle element of the list
    linkedlist.add("Middle")
    if "World" == linkedlist.find_middle():
        print("Test case 9 passed")
        count += 1
    else:
        print("Test case 9 failed")

    # Test case 10: Get nth node from the end (valid index)
    if "World" == linkedlist.nth_from_end(2):
        print("Test case 10 passed")
        count += 1
    else:
        print("Test case 10 failed")

    # Test case 11: Get nth node from the end (invalid index)
    if linkedlist.nth_from_end(4) is None:
        print("Test case 11 passed")
        count += 1
    else:
        print("Test case 11 failed")

    # Test case 12: Insert at position 1
    linkedlist.insert_at_position(1, "Inserted")
    if "[Hello][Inserted][World][Middle]" == linkedlist.to_string():
        print("Test case 12 passed")
        count += 1
    else:
        print("Test case 12 failed")

    # Test case 13: Insert at position 0
    linkedlist.insert_at_position(0, "Start")
    if "[Start][Hello][Inserted][World][Middle]" == linkedlist.to_string():
        print("Test case 13 passed")
        count += 1
    else:
        print("Test case 13 failed")

    # Test case 14: Insert at invalid position
    linkedlist.insert_at_position(10, "Invalid")
    if "[Start][Hello][Inserted][World][Middle]" == linkedlist.to_string():
        print("Test case 14 passed")
        count += 1
    else:
        print("Test case 14 failed")

    # Test case 15: Insert before an element
    linkedlist.insert_before("World", "BeforeWorld")
    if "[Start][Hello][Inserted][BeforeWorld][World][Middle]" == linkedlist.to_string():
        print("Test case 15 passed")
        count += 1
    else:
        print("Test case 15 failed")

    # Test case 16: Insert before the first occurrence of the first element
    linkedlist.insert_before("Start", "BeforeStart")
    if "[BeforeStart][Start][Hello][Inserted][BeforeWorld][World][Middle]" == linkedlist.to_string():
        print("Test case 16 passed")
        count += 1
    else:
        print("Test case 16 failed")

    # Test case 17: Delete the node after an element
    linkedlist.delete_after("Inserted")
    if "[BeforeStart][Start][Hello][Inserted][World][Middle]" == linkedlist.to_string():
        print("Test case 17 passed")
        count += 1
    else:
        print("Test case 17 failed")

    # Test case 18: Delete after an element that is not found
    linkedlist.delete_after("NonExistent")
    if "[BeforeStart][Start][Hello][Inserted][World][Middle]" == linkedlist.to_string():
        print("Test case 18 passed")
        count += 1
    else:
        print("Test case 18 failed")

    # Test case 19: Remove all elements from the list
    linkedlist.clear()
    if "LinkedList is empty" == linkedlist.to_string():
        print("Test case 19 passed")
        count += 1
    else:
        print("Test case 19 failed")

    # Test case 20: Get first element from an empty list
    if linkedlist.get_first() is None:
        print("Test case 20 passed")
        count += 1
    else:
        print("Test case 20 failed")

    # Test case 21: Add a null element to the list
    linkedlist.add(None)
    if "[None]" == linkedlist.to_string():
        print("Test case 21 passed")
        count += 1
    else:
        print("Test case 21 failed")

    # Test case 22: Add an empty string to the list
    linkedlist.add("")
    if "[None][]".strip() == linkedlist.to_string().strip():
        print("Test case 22 passed")
        count += 1
    else:
        print("Test case 22 failed")

    # Test case 23: Add and remove all elements
    linkedlist.remove()
    linkedlist.remove()
    if "LinkedList is empty" == linkedlist.to_string():
        print("Test case 23 passed")
        count += 1
    else:
        print("Test case 23 failed")

    # Test case 24: Add multiple elements, then clear the list
    linkedlist.add("First")
    linkedlist.add("Second")
    linkedlist.add("Third")
    linkedlist.clear()
    if "LinkedList is empty" == linkedlist.to_string():
        print("Test case 24 passed")
        count += 1
    else:
        print("Test case 24 failed")

    # Test case 25: Add elements after clearing the list
    linkedlist.add("NewElement")
    if "[NewElement]" == linkedlist.to_string():
        print("Test case 25 passed")
        count += 1
    else:
        print("Test case 25 failed")

    # Test case 26: Check the size of an empty list
    if linkedlist.size == 1:
        print("Test case 26 passed")
        count += 1
    else:
        print("Test case 26 failed")

    # Test case 27: Add duplicate elements and check if they exist
    linkedlist.add("Hello")
    linkedlist.add("Hello")
    if linkedlist.contains("Hello"):
        print("Test case 27 passed")
        count += 1
    else:
        print("Test case 27 failed")

    # Test case 28: Add null and empty elements, and check if they exist
    linkedlist.add(None)
    linkedlist.add("")
    if linkedlist.contains(""):
        print("Test case 28 passed")
        count += 1
    else:
        print("Test case 28 failed")

    # Test case 29: Add and remove elements in different order
    linkedlist.add("First")
    linkedlist.remove()
    linkedlist.add("Second")
    if "[Hello][Hello][None][][First][Second]" == linkedlist.to_string():
        print("Test case 29 passed")
        count += 1
    else:
        print("Test case 29 failed")

    # Test case 30: Add elements, clear, then add again
    linkedlist.add("A")
    linkedlist.add("B")
    linkedlist.clear()
    linkedlist.add("C")
    if "[C]" == linkedlist.to_string():
        print("Test case 30 passed")
        count += 1
    else:
        print("Test case 30 failed")

    # Test case 31: Add and remove from a list with a single element
    linkedlist.add("OnlyOne")
    linkedlist.remove()
    linkedlist.remove()
    if "LinkedList is empty" == linkedlist.to_string():
        print("Test case 31 passed")
        count += 1
    else:
        print("Test case 31 failed")

    # Test case 32: Add an element after clearing the list
    linkedlist.clear()
    linkedlist.add("AfterClear")
    if "[AfterClear]" == linkedlist.to_string():
        print("Test case 32 passed")
        count += 1
    else:
        print("Test case 32 failed")

    # Test case 33: Test middle element for a list with even number of elements
    linkedlist.add("One")
    linkedlist.add("Two")
    linkedlist.add("Three")
    linkedlist.add("Four")
    if "Two" == linkedlist.find_middle():
        print("Test case 33 passed")
        count += 1
    else:
        print("Test case 33 failed")

    # Test case 34: Test middle element for a list with odd number of elements
    linkedlist.add("Five")
    if "Three" == linkedlist.find_middle():
        print("Test case 34 passed")
        count += 1
    else:
        print("Test case 34 failed")

    # Test case 35: Add elements and verify the list is not empty
    linkedlist.add("Test")
    if not "LinkedList is empty" == linkedlist.to_string():
        print("Test case 35 passed")
        count += 1
    else:
        print("Test case 35 failed")

    # Test case 36: Remove all elements one by one
    linkedlist.remove()
    linkedlist.remove()
    linkedlist.remove()
    linkedlist.remove()
    linkedlist.remove()
    linkedlist.remove()
    linkedlist.remove()
    if "LinkedList is empty" == linkedlist.to_string():
        print("Test case 36 passed")
        count += 1
    else:
        print("Test case 36 failed")

    # Test case 37: Add elements and remove them in reverse order
    linkedlist.add("Apple")
    linkedlist.add("Banana")
    linkedlist.add("Cherry")
    linkedlist.remove_last()
    linkedlist.remove_last()
    if "[Apple]" == linkedlist.to_string():
        print("Test case 37 passed")
        count += 1
    else:
        print("Test case 37 failed")

    # Test case 38: Check if removing from an empty list returns null
    r = linkedlist.remove()
    if r == "Apple":
        print("Test case 38 passed")
        count += 1
    else:
        print("Test case 38 failed")

    # Test case 39: Test removing and adding elements again
    linkedlist.add("First")
    linkedlist.add("Second")
    linkedlist.remove()
    linkedlist.add("Third")
    if "[Second][Third]" == linkedlist.to_string():
        print("Test case 39 passed")
        count += 1
    else:
        print("Test case 39 failed")

    # Test case 40: Add elements, then clear the list and check the size
    linkedlist.clear()
    if linkedlist.size == 0:
        print("Test case 40 passed")
        count += 1
    else:
        print("Test case 40 failed")

    # Test case 41: Add elements to an empty list and check the size
    linkedlist.add("Element")
    if linkedlist.size == 1:
        print("Test case 41 passed")
        count += 1
    else:
        print("Test case 41 failed")

    # Test case 42: Check if the list is empty after removing all elements
    linkedlist.remove()
    if "LinkedList is empty" == linkedlist.to_string():
        print("Test case 42 passed")
        count += 1
    else:
        print("Test case 42 failed")

    # Test case 43: Test inserting at the last position
    linkedlist.add("First")
    linkedlist.insert_at_position(linkedlist.size, "Last")
    if "[First][Last]" == linkedlist.to_string():
        print("Test case 43 passed")
        count += 1
    else:
        print("Test case 43 failed")

    # Test case 44: Add elements and then clear the list
    linkedlist.add("Test")
    linkedlist.clear()
    if "LinkedList is empty" == linkedlist.to_string():
        print("Test case 44 passed")
        count += 1
    else:
        print("Test case 44 failed")

    # Test case 45: Add elements, insert before, and verify
    linkedlist.add("First")
    linkedlist.add("Second")
    linkedlist.insert_before("Second", "BeforeSecond")
    if "[First][BeforeSecond][Second]" == linkedlist.to_string():
        print("Test case 45 passed")
        count += 1
    else:
        print("Test case 45 failed")

    # Test case 46: Insert at position 0 and check the first element
    linkedlist.insert_at_position(0, "Start")
    if "[Start][First][BeforeSecond][Second]" == linkedlist.to_string():
        print("Test case 46 passed")
        count += 1
    else:
        print("Test case 46 failed")

    # Test case 47: Check that deleting after non-existent elements doesn't change the list
    linkedlist.delete_after("NonExistent")
    if "[Start][First][BeforeSecond][Second]" == linkedlist.to_string():
        print("Test case 47 passed")
        count += 1
    else:
        print("Test case 47 failed")

    # Test case 48: Test inserting at position greater than size
    linkedlist.insert_at_position(linkedlist.size + 1, "Invalid")
    if "[Start][First][BeforeSecond][Second]" == linkedlist.to_string():
        print("Test case 48 passed")
        count += 1
    else:
        print("Test case 48 failed")

    # Test case 49: Test inserting an element before the first element
    linkedlist.insert_before("Start", "BeforeStart")
    if "[BeforeStart][Start][First][BeforeSecond][Second]" == linkedlist.to_string():
        print("Test case 49 passed")
        count += 1
    else:
        print("Test case 49 failed")

    # Test case 50: Ensure the list is still valid after many operations
    linkedlist.add("End")
    linkedlist.remove()
    linkedlist.remove_last()
    linkedlist.add("Final")
    if "[Start][First][BeforeSecond][Second][Final]" == linkedlist.to_string():
        print("Test case 50 passed")
        count += 1
    else:
        print("Test case 50 failed")

    print(f"Total passed test cases: {count}")


run_tests()
