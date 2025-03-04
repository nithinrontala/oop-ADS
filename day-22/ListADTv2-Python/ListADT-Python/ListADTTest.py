from Solution import ArrayListADT

# Testing the ArrayListADT implementation in Python.
if __name__ == "__main__":
    listADT = ArrayListADT()
    all_tests_passed = True

    # Test add(e)
    listADT.add(10)
    listADT.add(20)
    listADT.add(30)
    # listADT.add("abc")
    if str(listADT) == "[10, 20, 30]":
        print("Test add(e) Passed")
    else:
        print("Test add(e) Failed:", str(listADT))
        all_tests_passed = False

    # Test add_at(index, element)
    listADT.add_at(0, 5)      # -> [5, 10, 20, 30]
    listADT.add_at(2, 15)     # -> [5, 10, 15, 20, 30]
    listADT.add_at(listADT.size, 35)  # -> [5, 10, 15, 20, 30, 35]
    if str(listADT) == "[5, 10, 15, 20, 30, 35]":
        print("Test add_at(index, element) Passed")
    else:
        print("Test add_at(index, element) Failed:", str(listADT))
        all_tests_passed = False

    # Test add_all_at(index, collection)
    coll1 = [100, 200, 300]
    listADT.add_all_at(3, coll1)
    expected = "[5, 10, 15, 100, 200, 300, 20, 30, 35]"
    if str(listADT) == expected:
        print("Test add_all_at(index, collection) Passed")
    else:
        print("Test add_all_at(index, collection) Failed:", str(listADT))
        all_tests_passed = False

    # Test add_all(collection)
    coll2 = [400, 500]
    listADT.add_all(coll2)
    expected = "[5, 10, 15, 100, 200, 300, 20, 30, 35, 400, 500]"
    if str(listADT) == expected:
        print("Test add_all(collection) Passed")
    else:
        print("Test add_all(collection) Failed:", str(listADT))
        all_tests_passed = False

    # Test contains(o)
    if listADT.contains(100) and not listADT.contains(999):
        print("Test contains(o) Passed")
    else:
        print("Test contains(o) Failed")
        all_tests_passed = False

    # Test ensure_capacity(min_capacity)
    old_capacity = len(listADT.data)
    listADT.ensure_capacity(old_capacity + 50)
    if len(listADT.data) >= old_capacity + 50:
        print("Test ensure_capacity() Passed")
    else:
        print("Test ensure_capacity() Failed")
        all_tests_passed = False

    # Test get(index)
    if listADT.get(0) == 5 and listADT.get(3) == 100 and listADT.get(listADT.size - 1) == 500:
        print("Test get(index) Passed")
    else:
        print("Test get(index) Failed")
        all_tests_passed = False

    # Test index_of(o) and last_index_of(o)
    listADT.add(100)  # duplicate element for testing
    # print(121212121,listADT.size-1)
    if listADT.index_of(100) == 3 and listADT.last_index_of(100) == listADT.size - 1:
        print("Test index_of() and last_index_of() Passed")
    else:
        print("Test index_of() and/or last_index_of() Failed: index_of(100) =", listADT.index_of(100),
              ", last_index_of(100) =", listADT.last_index_of(100))
        all_tests_passed = False

    # Test is_empty() and size_()
    # print(123456,listADT.size,listADT.size_())
    # print(1232323212,listADT.is_empty())
    if not listADT.is_empty() and listADT.size_() == listADT.size:
        print("Test is_empty() and size_() Passed")
    else:
        print("Test is_empty() and/or size_() Failed")
        all_tests_passed = False

    # Test remove_at(index)
    removed = listADT.remove_at(0)  # remove first element (5)
    if removed == 5 and listADT.index_of(5) == -1:
        print("Test remove_at(index) Passed")
    else:
        print("Test remove_at(index) Failed:", str(listADT))
        all_tests_passed = False

    # Test remove(o)
    if listADT.remove(100):  # remove first occurrence of 100
        print("Test remove(o) Passed")
    else:
        print("Test remove(o) Failed:", str(listADT))
        all_tests_passed = False

    # Test set(index, element)
    old_val = listADT.set(2, 999)
    if old_val is not None and listADT.get(2) == 999:
        print("Test set(index, element) Passed")
    else:
        print("Test set(index, element) Failed:", str(listADT))
        all_tests_passed = False

    # Test trim_to_size()
    listADT.trim_to_size()
    if len(listADT.data) == listADT.size:
        print("Test trim_to_size() Passed")
    else:
        print("Test trim_to_size() Failed: capacity =", len(listADT.data), ", size =", listADT.size)
        all_tests_passed = False

    # Test clear()
    listADT.clear()
    if listADT.is_empty() and str(listADT) == "[]":
        print("Test clear() Passed")
    else:
        print("Test clear() Failed:", str(listADT))
        all_tests_passed = False

    if all_tests_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed. Please review the output above.")
