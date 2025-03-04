
from Solution import ArrayListADT

# Testing the ArrayListADT implementation
def main():
    # Instantiate our list
    listADT = ArrayListADT()
    testPassed = True

    # Test 1: add(e)
    listADT.add(10)
    listADT.add(20)
    listADT.add(30)
    if str(listADT) == "[10, 20, 30]":
        print("Test 1 Passed: add(e) works correctly.")
    else:
        print("Test 1 Failed: add(e) output:", str(listADT))
        testPassed = False

    # Test 2: add_at(index, element)
    # Insert at beginning.
    listADT.add_at(0, 5)  # Expected: [5, 10, 20, 30]
    if str(listADT) == "[5, 10, 20, 30]":
        print("Test 2a Passed: add_at at beginning works correctly.")
    else:
        print("Test 2a Failed: add_at at beginning output:", str(listADT))
        testPassed = False

    # Insert in middle.
    listADT.add_at(2, 15)  # Expected: [5, 10, 15, 20, 30]
    if str(listADT) == "[5, 10, 15, 20, 30]":
        print("Test 2b Passed: add_at in middle works correctly.")
    else:
        print("Test 2b Failed: add_at in middle output:", str(listADT))
        testPassed = False

    # Insert at end.
    listADT.add_at(listADT.size, 35)  # Expected: [5, 10, 15, 20, 30, 35]
    if str(listADT) == "[5, 10, 15, 20, 30, 35]":
        print("Test 2c Passed: add_at at end works correctly.")
    else:
        print("Test 2c Failed: add_at at end output:", str(listADT))
        testPassed = False

    # Test 3: addAll(index, collection)
    # Create a collection (Python list) of integers.
    collection = [100, 200, 300]
    # Insert collection at index 3.
    listADT.addAll(3, collection)
    # Expected: [5, 10, 15, 100, 200, 300, 20, 30, 35]
    expectedAfterAddAll = "[5, 10, 15, 100, 200, 300, 20, 30, 35]"
    if str(listADT) == expectedAfterAddAll:
        print("Test 3 Passed: addAll(index, collection) works correctly.")
    else:
        print("Test 3 Failed: addAll(index, collection) output:", str(listADT))
        testPassed = False

    # Test 4: contains(o)
    # Check for an element that exists.
    if listADT.contains(100):
        print("Test 4a Passed: contains() correctly returns True for an existing element.")
    else:
        print("Test 4a Failed: contains() did not find an existing element (100).")
        testPassed = False

    # Check for an element that does not exist.
    if not listADT.contains(999):
        print("Test 4b Passed: contains() correctly returns False for a non-existing element.")
    else:
        print("Test 4b Failed: contains() incorrectly found a non-existing element (999).")
        testPassed = False

    # Test 5: get(index)
    # Get first element.
    if listADT.get(0) == 5:
        print("Test 5a Passed: get(0) works correctly.")
    else:
        print("Test 5a Failed: get(0) returned:", listADT.get(0))
        testPassed = False

    # Get an element in the middle.
    if listADT.get(3) == 100:
        print("Test 5b Passed: get(3) works correctly.")
    else:
        print("Test 5b Failed: get(3) returned:", listADT.get(3))
        testPassed = False

    # Get last element.
    if listADT.get(listADT.size - 1) == 35:
        print("Test 5c Passed: get(last index) works correctly.")
    else:
        print("Test 5c Failed: get(last index) returned:", listADT.get(listADT.size - 1))
        testPassed = False

    # Test 6: ensureCapacity(minCapacity)
    old_capacity = len(listADT.data)
    listADT.ensureCapacity(old_capacity + 50)
    if len(listADT.data) >= old_capacity + 50:
        print("Test 6 Passed: ensureCapacity() increased the capacity as expected.")
    else:
        print("Test 6 Failed: ensureCapacity() did not increase the capacity correctly.")
        testPassed = False

    # Test 7: clear()
    listADT.clear()
    if str(listADT) == "[]" and listADT.size == 0:
        print("Test 7 Passed: clear() works correctly.")
    else:
        print("Test 7 Failed: clear() output:", str(listADT), "size:", listADT.size)
        testPassed = False

    # Test 8: Handling of None values (similar to null in Java)
    listADT.add(None)
    listADT.add(50)
    if listADT.contains(None) and listADT.get(0) is None and str(listADT) == "[None, 50]":
        print("Test 8 Passed: Handling of None values works correctly.")
    else:
        print("Test 8 Failed: Handling of None values output:", str(listADT))
        testPassed = False

    if testPassed:
        print("All tests passed!")
    else:
        print("Some tests failed. Please review the output for details.")

main()