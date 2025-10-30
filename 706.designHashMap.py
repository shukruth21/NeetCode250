class MyHashMap:

    def __init__(self):
        self.size = 10**6 + 1
        self.data = [None]*self.size

    def put(self, key: int, value: int) -> None:
        self.data[key]=value

    def get(self, key: int) -> int:
        return -1 if self.data[key] is None else self.data[key]

    def remove(self, key: int) -> None:
        self.data[key]=None
