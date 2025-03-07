from Solution import CircularLinkedList

def run_tests():
    count = 0
    cll = CircularLinkedList()

    # Test case 1: add
    cll.add("Hello World")
    if str(cll) == "[Hello World]":
        print("Test case 1 passed")
        count += 1
    else:
        print("Test case 1 failed")

    # Test case 2: add_first
    cll.add_first("Circular List")
    if str(cll) == "[Circular List]<->[Hello World]":
        print("Test case 2 passed")
        count += 1
    else:
        print("Test case 2 failed")

    # Test case 3: add another element
    cll.add("Data Structure")
    if str(cll) == "[Circular List]<->[Hello World]<->[Data Structure]":
        print("Test case 3 passed")
        count += 1
    else:
        print("Test case 3 failed")

    # Test case 4: contains (intentional typo to return False)
    if not cll.contains("Data Structur"):
        print("Test case 4 passed")
        count += 1
    else:
        print("Test case 4 failed")

    # Test case 5: get_first
    if cll.get_first() == "Circular List":
        print("Test case 5 passed")
        count += 1
    else:
        print("Test case 5 failed")

    # Test case 6: get_last
    if cll.get_last() == "Data Structure":
        print("Test case 6 passed")
        count += 1
    else:
        print("Test case 6 failed")

    # Test case 7: size
    if cll.size() == 3:
        print("Test case 7 passed")
        count += 1
    else:
        print("Test case 7 failed")

    # Test case 8: remove (remove first element)
    removed = cll.remove()
    if removed == "Circular List" and str(cll) == "[Hello World]<->[Data Structure]":
        print("Test case 8 passed")
        count += 1
    else:
        print("Test case 8 failed")

    # Test case 9: remove_last (remove last element)
    removed_last = cll.remove_last()
    if removed_last == "Data Structure" and str(cll) == "[Hello World]":
        print("Test case 9 passed")
        count += 1
    else:
        print("Test case 9 failed")

    # Test case 10: get(index)
    if cll.get(0) == "Hello World":
        print("Test case 10 passed")
        count += 1
    else:
        print("Test case 10 failed")

    # Test case 11: clear
    cll.remove()  # remove remaining element
    cll.clear()
    if str(cll) == "CircularLinkedList is empty" and cll.size() == 0:
        print("Test case 11 passed")
        count += 1
    else:
        print("Test case 11 failed")

    # Test case 12: Check circular nature
    cll.add("A")
    cll.add("B")
    cll.add("C")
    if cll.is_circular():
        print("Test case 12 (circular check) passed")
        count += 1
    else:
        print("Test case 12 (circular check) failed")

    print("Total testcases passed:", count)


run_tests()
