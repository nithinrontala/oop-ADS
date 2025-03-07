from Solution import DoublyLinkedList

def run_tests():    
    count = 0
    dll = DoublyLinkedList()

    # Test case 1: add
    dll.add("Hello World")
    # print(str(dll))
    if str(dll) == "[Hello World]":
        print("Test case 1 passed")
        count += 1
    else:
        print("Test case 1 failed")

    # Test case 2: add_first
    dll.add_first("Doubly List")
    if str(dll) == "[Doubly List]<->[Hello World]":
        print("Test case 2 passed")
        count += 1
    else:
        print("Test case 2 failed")

    # Test case 3: add another element
    dll.add("Data Structure")
    if str(dll) == "[Doubly List]<->[Hello World]<->[Data Structure]":
        print("Test case 3 passed")
        count += 1
    else:
        print("Test case 3 failed")

    # Test case 4: contains
    if not dll.contains("Data Structur"):
        print("Test case 4 passed")
        count += 1
    else:
        print("Test case 4 failed")

    # Test case 5: get_first
    if dll.get_first() == "Doubly List":
        print("Test case 5 passed")
        count += 1
    else:
        print("Test case 5 failed")

    # Test case 6: get_last
    # print(dll.get_last())
    if dll.get_last() == "Data Structure":
        print("Test case 6 passed")
        count += 1
    else:
        print("Test case 6 failed")

    # Test case 7: size
    if dll.size() == 3:
        print("Test case 7 passed")
        count += 1
    else:
        print("Test case 7 failed")

    # Test case 8: remove (remove first element)
    removed = dll.remove()
    # print(str(dll))
    if removed == "Doubly List" and str(dll) == "[Hello World]<->[Data Structure]":
        print("Test case 8 passed")
        count += 1
    else:
        print("Test case 8 failed")

    # Test case 9: remove_last (remove last element)
    removed_last = dll.remove_last()
    # print(str(dll))
    if removed_last == "Data Structure" and str(dll) == "[Hello World]":
        print("Test case 9 passed")
        count += 1
    else:
        print("Test case 9 failed")

    # Test case 10: get(index)
    if dll.get(0) == "Hello World":
        print("Test case 10 passed")
        count += 1
    else:
        print("Test case 10 failed")

    # Test case 11: clear
    dll.remove()  # remove remaining element
    dll.clear()
    if str(dll) == "DoublyLinkedList is empty" and dll.size() == 0:
        print("Test case 11 passed")
        count += 1
    else:
        print("Test case 11 failed")

    print("Total testcases passed:", count)


run_tests()
