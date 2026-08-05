class MinStack:

    def __init__(self):
        self.item = []

    def push(self, val: int) -> None:
        self.item.append(val)


    def pop(self) -> None:
        del self.item[-1]
        

    def top(self) -> int:
        return self.item[-1]
        

    def getMin(self) -> int:
        return min(self.item)