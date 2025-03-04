# from typing import Generic, TypeVar, List, Optional, Collection

# T = TypeVar('T')

# class ArrayListADT(Generic[T]):
#     def __init__(self, initial_capacity: int = 10) -> None:
#         self._data: List[Optional[T]] = [None] * initial_capacity
#         self._size: int = 0

#     def size(self) -> int:
#         return self._size

#     def _resize(self, new_capacity: int) -> None:
#         new_data: List[Optional[T]] = [None] * new_capacity
#         for i in range(self._size):
#             new_data[i] = self._data[i]
#         self._data = new_data

#     def ensure_capacity(self, min_capacity: int) -> None:
#         if len(self._data) < min_capacity:
#             self._resize(min_capacity)

#     def trim_to_size(self) -> None:
#         self._resize(self._size)

#     def add(self, e: T) -> bool:
#         if self._size == len(self._data):
#             self._resize(len(self._data) * 2)
#         self._data[self._size] = e
#         self._size += 1
#         return True

#     def add_at(self, index: int, element: T) -> None:
#         if index < 0 or index > self._size:
#             raise IndexError("Index out of bounds")
#         if self._size == len(self._data):
#             self._resize(len(self._data) * 2)
#         for i in range(self._size, index, -1):
#             self._data[i] = self._data[i - 1]
#         self._data[index] = element
#         self._size += 1

#     def add_all(self, collection: Collection[T]) -> bool:
#         for item in collection:
#             self.add(item)
#         return True

#     def add_all_at(self, index: int, collection: Collection[T]) -> bool:
#         if index < 0 or index > self._size:
#             raise IndexError("Index out of bounds")
#         for item in collection:
#             self.add_at(index, item)
#             index += 1
#         return True

#     def get(self, index: int) -> T:
#         if index < 0 or index >= self._size:
#             raise IndexError("Index out of bounds")
#         return self._data[index]  # type: ignore

#     def set(self, index: int, element: T) -> T:
#         if index < 0 or index >= self._size:
#             raise IndexError("Index out of bounds")
#         old_value = self._data[index]
#         self._data[index] = element
#         return old_value  # type: ignore

#     def remove_at(self, index: int) -> T:
#         if index < 0 or index >= self._size:
#             raise IndexError("Index out of bounds")
#         removed_element = self._data[index]  # type: ignore
#         for i in range(index, self._size - 1):
#             self._data[i] = self._data[i + 1]
#         self._data[self._size - 1] = None
#         self._size -= 1
#         return removed_element

#     def remove(self, o: T) -> bool:
#         for index in range(self._size):
#             if self._data[index] == o:
#                 self.remove_at(index)
#                 return True
#         return False

#     def clear(self) -> None:
#         self._data = [None] * len(self._data)
#         self._size = 0

#     def contains(self, o: T) -> bool:
#         for i in range(self._size):
#             if self._data[i] == o:
#                 return True
#         return False

#     def index_of(self, o: T) -> int:
#         for index in range(self._size):
#             if self._data[index] == o:
#                 return index
#         return -1

#     def last_index_of(self, o: T) -> int:
#         for index in range(self._size - 1, -1, -1):
#             if self._data[index] == o:
#                 return index
#         return -1

#     def is_empty(self) -> bool:
#         return self._size == 0

#     def __str__(self) -> str:
#         return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + "]"

from Solution import ArrayListADT
# Test cases for integer, string, and float lists.
def test_integer_list():
    print("=== Testing ArrayListADT[int] ===")
    list_int = ArrayListADT[int]()
    all_tests_passed = True

    # Test add(T)
    list_int.add(10)
    list_int.add(20)
    list_int.add(30)
    if str(list_int) == "[10, 20, 30]":
        print("Test add(T) Passed")
    else:
        print("Test add(T) Failed:", list_int)
        all_tests_passed = False

    # Test add_at(index, element)
    list_int.add_at(0, 5)      # [5, 10, 20, 30]
    list_int.add_at(2, 15)     # [5, 10, 15, 20, 30]
    list_int.add_at(list_int.size(), 35)  # [5, 10, 15, 20, 30, 35]
    if str(list_int) == "[5, 10, 15, 20, 30, 35]":
        print("Test add_at(index, element) Passed")
    else:
        print("Test add_at(index, element) Failed:", list_int)
        all_tests_passed = False

    # Test add_all_at(index, collection)
    coll1 = [100, 200, 300]
    list_int.add_all_at(3, coll1)
    # Expected: [5, 10, 15, 100, 200, 300, 20, 30, 35]
    if str(list_int) == "[5, 10, 15, 100, 200, 300, 20, 30, 35]":
        print("Test add_all_at(index, collection) Passed")
    else:
        print("Test add_all_at(index, collection) Failed:", list_int)
        all_tests_passed = False

    # Test add_all(collection)
    coll2 = [400, 500]
    list_int.add_all(coll2)
    # Expected: [5, 10, 15, 100, 200, 300, 20, 30, 35, 400, 500]
    if str(list_int) == "[5, 10, 15, 100, 200, 300, 20, 30, 35, 400, 500]":
        print("Test add_all(collection) Passed")
    else:
        print("Test add_all(collection) Failed:", list_int)
        all_tests_passed = False

    # Test contains(o)
    if list_int.contains(100) and not list_int.contains(999):
        print("Test contains(o) Passed")
    else:
        print("Test contains(o) Failed")
        all_tests_passed = False

    # Test ensure_capacity(min_capacity)
    old_capacity = len(list_int._data)
    list_int.ensure_capacity(old_capacity + 50)
    if len(list_int._data) >= old_capacity + 50:
        print("Test ensure_capacity(min_capacity) Passed")
    else:
        print("Test ensure_capacity(min_capacity) Failed")
        all_tests_passed = False

    # Test get(index)
    if list_int.get(0) == 5 and list_int.get(3) == 100 and list_int.get(list_int.size() - 1) == 500:
        print("Test get(index) Passed")
    else:
        print("Test get(index) Failed")
        all_tests_passed = False

    # Test index_of(o) and last_index_of(o)
    list_int.add(100)  # duplicate element
    if list_int.index_of(100) == 3 and list_int.last_index_of(100) == list_int.size() - 1:
        print("Test index_of(o) and last_index_of(o) Passed")
    else:
        print("Test index_of(o) and last_index_of(o) Failed: index_of(100) =", list_int.index_of(100),
              "last_index_of(100) =", list_int.last_index_of(100))
        all_tests_passed = False

    # Test remove_at(index)
    removed = list_int.remove_at(0)  # remove first element (5)
    print(1234323423,list_int.index_of(5) == -1,removed == 5)
    if removed == 5 and list_int.index_of(5) == -1:
        print("Test remove_at(index) Passed")
    else:
        print("Test remove_at(index) Failed: removed =", removed, ", list =", list_int)
        all_tests_passed = False

    # Test remove(o)
    removed_flag = list_int.remove(100)  # removes first occurrence of 100
    if removed_flag:
        print("Test remove(o) Passed")
    else:
        print("Test remove(o) Failed:", list_int)
        all_tests_passed = False

    # Test set(index, element)
    old_val = list_int.set(2, 999)
    if old_val is not None and list_int.get(2) == 999:
        print("Test set(index, element) Passed")
    else:
        print("Test set(index, element) Failed: old_val =", old_val, ", list =", list_int)
        all_tests_passed = False

    # Test trim_to_size()
    list_int.trim_to_size()
    # print(1234,list_int.size())
    if len(list_int._data) == list_int.size():
        print("Test trim_to_size() Passed")
    else:
        print("Test trim_to_size() Failed: capacity =", len(list_int._data), ", size =", list_int.size())
        all_tests_passed = False

    # Test clear()
    list_int.clear()
    if list_int.is_empty() and str(list_int) == "[]":
        print("Test clear() Passed")
    else:
        print("Test clear() Failed:", list_int)
        all_tests_passed = False

    if all_tests_passed:
        print("All Integer tests passed successfully!\n")
    else:
        print("Some Integer tests failed. Please review the output above.\n")


def test_string_list():
    print("=== Testing ArrayListADT[str] ===")
    list_str = ArrayListADT[str]()
    all_tests_passed = True

    # Test add(T)
    list_str.add("apple")
    list_str.add("banana")
    list_str.add("cherry")
    if str(list_str) == "[apple, banana, cherry]":
        print("Test add(T) Passed")
    else:
        print("Test add(T) Failed:", list_str)
        all_tests_passed = False

    # Test add_at(index, element)
    list_str.add_at(0, "avocado")  # [avocado, apple, banana, cherry]
    list_str.add_at(2, "blueberry")  # [avocado, apple, blueberry, banana, cherry]
    list_str.add_at(list_str.size(), "date")  # [avocado, apple, blueberry, banana, cherry, date]
    if str(list_str) == "[avocado, apple, blueberry, banana, cherry, date]":
        print("Test add_at(index, element) Passed")
    else:
        print("Test add_at(index, element) Failed:", list_str)
        all_tests_passed = False

    # Test add_all_at(index, collection)
    coll1 = ["kiwi", "lemon", "mango"]
    list_str.add_all_at(3, coll1)
    # Expected: [avocado, apple, blueberry, kiwi, lemon, mango, banana, cherry, date]
    if str(list_str) == "[avocado, apple, blueberry, kiwi, lemon, mango, banana, cherry, date]":
        print("Test add_all_at(index, collection) Passed")
    else:
        print("Test add_all_at(index, collection) Failed:", list_str)
        all_tests_passed = False

    # Test add_all(collection)
    coll2 = ["nectarine", "orange"]
    list_str.add_all(coll2)
    # Expected: [avocado, apple, blueberry, kiwi, lemon, mango, banana, cherry, date, nectarine, orange]
    if str(list_str) == "[avocado, apple, blueberry, kiwi, lemon, mango, banana, cherry, date, nectarine, orange]":
        print("Test add_all(collection) Passed")
    else:
        print("Test add_all(collection) Failed:", list_str)
        all_tests_passed = False

    # Test contains(o)
    if list_str.contains("kiwi") and not list_str.contains("papaya"):
        print("Test contains(o) Passed")
    else:
        print("Test contains(o) Failed")
        all_tests_passed = False

    # Test get(index)
    if list_str.get(0) == "avocado" and list_str.get(3) == "kiwi" and list_str.get(list_str.size() - 1) == "orange":
        print("Test get(index) Passed")
    else:
        print("Test get(index) Failed")
        all_tests_passed = False

    # Test index_of(o) and last_index_of(o)
    list_str.add("kiwi")  # duplicate element
    if list_str.index_of("kiwi") == 3 and list_str.last_index_of("kiwi") == list_str.size() - 1:
        print("Test index_of(o) and last_index_of(o) Passed")
    else:
        print("Test index_of(o) and last_index_of(o) Failed: index_of(kiwi) =", list_str.index_of("kiwi"),
              "last_index_of(kiwi) =", list_str.last_index_of("kiwi"))
        all_tests_passed = False

    # Test remove_at(index)
    removed = list_str.remove_at(0)  # remove "avocado"
    if removed == "avocado" and not list_str.contains("avocado"):
        print("Test remove_at(index) Passed")
    else:
        print("Test remove_at(index) Failed: removed =", removed, ", list =", list_str)
        all_tests_passed = False

    # Test remove(o)
    removed_flag = list_str.remove("kiwi")  # removes first occurrence of "kiwi"
    if removed_flag:
        print("Test remove(o) Passed")
    else:
        print("Test remove(o) Failed:", list_str)
        all_tests_passed = False

    # Test set(index, element)
    old_val = list_str.set(2, "papaya")
    if old_val is not None and list_str.get(2) == "papaya":
        print("Test set(index, element) Passed")
    else:
        print("Test set(index, element) Failed: old_val =", old_val, ", list =", list_str)
        all_tests_passed = False

    # Test trim_to_size()
    list_str.trim_to_size()
    if len(list_str._data) == list_str.size():
        print("Test trim_to_size() Passed")
    else:
        print("Test trim_to_size() Failed: capacity =", len(list_str._data), ", size =", list_str.size())
        all_tests_passed = False

    # Test clear()
    list_str.clear()
    if list_str.is_empty() and str(list_str) == "[]":
        print("Test clear() Passed")
    else:
        print("Test clear() Failed:", list_str)
        all_tests_passed = False

    if all_tests_passed:
        print("All String tests passed successfully!\n")
    else:
        print("Some String tests failed. Please review the output above.\n")


def test_float_list():
    print("=== Testing ArrayListADT[float] ===")
    list_float = ArrayListADT[float]()
    all_tests_passed = True

    # Test add(T)
    list_float.add(1.1)
    list_float.add(2.2)
    list_float.add(3.3)
    if str(list_float) == "[1.1, 2.2, 3.3]":
        print("Test add(T) Passed")
    else:
        print("Test add(T) Failed:", list_float)
        all_tests_passed = False

    # Test add_at(index, element)
    list_float.add_at(0, 0.5)   # [0.5, 1.1, 2.2, 3.3]
    list_float.add_at(2, 1.5)   # [0.5, 1.1, 1.5, 2.2, 3.3]
    list_float.add_at(list_float.size(), 4.4)  # [0.5, 1.1, 1.5, 2.2, 3.3, 4.4]
    if str(list_float) == "[0.5, 1.1, 1.5, 2.2, 3.3, 4.4]":
        print("Test add_at(index, element) Passed")
    else:
        print("Test add_at(index, element) Failed:", list_float)
        all_tests_passed = False

    # Test add_all_at(index, collection)
    coll1 = [5.5, 6.6, 7.7]
    list_float.add_all_at(3, coll1)
    # Expected: [0.5, 1.1, 1.5, 5.5, 6.6, 7.7, 2.2, 3.3, 4.4]
    if str(list_float) == "[0.5, 1.1, 1.5, 5.5, 6.6, 7.7, 2.2, 3.3, 4.4]":
        print("Test add_all_at(index, collection) Passed")
    else:
        print("Test add_all_at(index, collection) Failed:", list_float)
        all_tests_passed = False

    # Test add_all(collection)
    coll2 = [8.8, 9.9]
    list_float.add_all(coll2)
    # Expected: [0.5, 1.1, 1.5, 5.5, 6.6, 7.7, 2.2, 3.3, 4.4, 8.8, 9.9]
    if str(list_float) == "[0.5, 1.1, 1.5, 5.5, 6.6, 7.7, 2.2, 3.3, 4.4, 8.8, 9.9]":
        print("Test add_all(collection) Passed")
    else:
        print("Test add_all(collection) Failed:", list_float)
        all_tests_passed = False

    # Test contains(o)
    if list_float.contains(5.5) and not list_float.contains(10.0):
        print("Test contains(o) Passed")
    else:
        print("Test contains(o) Failed")
        all_tests_passed = False

    # Test get(index)
    if list_float.get(0) == 0.5 and list_float.get(3) == 5.5 and list_float.get(list_float.size() - 1) == 9.9:
        print("Test get(index) Passed")
    else:
        print("Test get(index) Failed")
        all_tests_passed = False

    # Test index_of(o) and last_index_of(o)
    list_float.add(5.5)  # duplicate element
    # print(123e21232123,list_float.size() - 1)
    if list_float.index_of(5.5) == 3 and list_float.last_index_of(5.5) == list_float.size() - 1:
        print("Test index_of(o) and last_index_of(o) Passed")
    else:
        print("Test index_of(o) and last_index_of(o) Failed: index_of(5.5) =", list_float.index_of(5.5),
              "last_index_of(5.5) =", list_float.last_index_of(5.5))
        all_tests_passed = False

    # Test remove_at(index)
    removed = list_float.remove_at(0)  # remove first element (0.5)
    if removed == 0.5 and not list_float.contains(0.5):
        print("Test remove_at(index) Passed")
    else:
        print("Test remove_at(index) Failed: removed =", removed, ", list =", list_float)
        all_tests_passed = False

    # Test remove(o)
    removed_flag = list_float.remove(5.5)  # removes first occurrence of 5.5
    if removed_flag:
        print("Test remove(o) Passed")
    else:
        print("Test remove(o) Failed:", list_float)
        all_tests_passed = False

    # Test set(index, element)
    old_val = list_float.set(2, 10.10)
    if old_val is not None and list_float.get(2) == 10.10:
        print("Test set(index, element) Passed")
    else:
        print("Test set(index, element) Failed: old_val =", old_val, ", list =", list_float)
        all_tests_passed = False

    # Test trim_to_size()
    list_float.trim_to_size()
    if len(list_float._data) == list_float.size():
        print("Test trim_to_size() Passed")
    else:
        print("Test trim_to_size() Failed: capacity =", len(list_float._data), ", size =", list_float.size())
        all_tests_passed = False

    # Test clear()
    list_float.clear()
    if list_float.is_empty() and str(list_float) == "[]":
        print("Test clear() Passed")
    else:
        print("Test clear() Failed:", list_float)
        all_tests_passed = False

    if all_tests_passed:
        print("All Float tests passed successfully!\n")
    else:
        print("Some Float tests failed. Please review the output above.\n")


if __name__ == "__main__":
    test_integer_list()
    test_string_list()
    test_float_list()
