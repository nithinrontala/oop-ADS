from typing import Generic, TypeVar, List, Optional, Collection

T = TypeVar('T')

class ArrayListADT(Generic[T]):
    def __init__(self, initial_capacity: int = 10) -> None:
        self._data: List[Optional[T]] = [None] * initial_capacity
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def _resize(self, new_capacity: int) -> None:
        new : List[Optional[T]] = [None] * new_capacity
        for i in range(self._size):
            new[i] = self._data[i]
        self._data = new

    def ensure_capacity(self, min_capacity: int) -> None:
        if len(self._data) < min_capacity:
            self._resize(min_capacity)

    def trim_to_size(self) -> None:
        self._resize(self._size)

    def add(self, e: T) -> bool:
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        for i in range(len(self._data)):
            if self._data[i]== None:
                self._data[i] = e
                self._size+=1
                return True

    def add_at(self, index: int, element: T) -> None:
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        index = int(index)  
        self._data.append(element)  
        self._size+=1
        for i in range(len(self._data) - 2, index - 1, -1):
            self._data[i + 1] = self._data[i]
        
        self._data[index] = element

    def add_all(self, collection: Collection[T]) -> bool:
        for i in collection:
            self.add(i)
        return True
    def add_all_at(self, index: int, collection: Collection[T]) -> bool:
        for i in range(len(collection)):
            self.add_at(index + i, collection[i])
        return True

    def get(self, index: int) -> T:
        return self._data[index]

    def set(self, index: int, element: T) -> T:
        a = self._data[index]
        self._data[index] = element
        return a

    def remove_at(self, index: int) -> T:
        l = []
        a = self._data[index]
        for i in range(len(self._data)):
            if i != index:
                l.append(self._data[i])
        self._data = l
        self._size = len(self._data)
        return a


    def remove(self, o: T) -> bool:
        a = self._data.index(o)
        self.remove_at(a)
        self._size-=1
        return True

    def clear(self) -> None:
        self._data = []
        self._size = 0

    def contains(self, o: T) -> bool:
        for i in self._data:
            if i == o:
                return True
        return False 

    def index_of(self, o: T) -> int:
        # print(123232123232,self._data)
        for i in range(len(self._data)):
            if self._data[i] == o:
                return i
        return -1

    def last_index_of(self, o: T) -> int:
        for i in range(len(self._data)-1,0,-1):
            if self._data[i] == o:
                return i
        return -1
            
    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __str__(self) -> str:
        return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + "]"


