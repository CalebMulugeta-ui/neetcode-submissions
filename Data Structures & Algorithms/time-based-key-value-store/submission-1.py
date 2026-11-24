from collections import defaultdict
class TimeMap:
  

    def __init__(self):
        self.keyMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        valueList = self.keyMap[key]
        for i in valueList:
            if i[1] == timestamp:
                return i[0]
        
        
        for i in range(len(valueList)-1,-1,-1):
            if valueList[i][1] > timestamp:
                continue
            else:
                return valueList[i][0]
        
        return ""

