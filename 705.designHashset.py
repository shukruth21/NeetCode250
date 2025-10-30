class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if(key not in self.data):
            self.data.append(key)

    def remove(self, key: int) -> None:
        if(key in self.data):
            self.data.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.data


Boolean Array

class MyHashSet:

    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]
Time & Space Complexity
Time complexity: 
O(1)
O(1) for each function call.
Space complexity: 
O(1000000)
O(1000000) since the key is in the range [0,1000000]
