class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        arr = []
        arr.append(0)
        self.largest = k
        for i in nums:
            #if min heap isnt k long
            if (len(arr)-1) < k:
                arr.append(i)
                e = len(arr) - 1
                #procolate up to create min heap
                while e > 1 and arr[e] < arr [e//2]:
                    temp = arr[e//2]
                    arr[e//2] = arr[e]
                    arr[e] = temp
                    e = e//2
            else:
                #check if current num is bigger than minimum of min heap
                if i > arr[1]:
                    #change the minimum of the min heap too the curr num
                    j = 1
                    arr[j] = i
                    #procalate down
                    while (j*2) < len(arr):
                        if j*2+1 < len(arr) and arr[j] > arr[j*2+1] and arr[j*2+1] < arr[j*2]:
                            temp = arr[j*2+1]
                            arr[j*2+1] = arr[j]
                            arr[j] = temp
                            j  = j*2+1
                        elif arr[j] > arr[j*2]:
                            temp = arr[j*2]
                            arr[j*2] = arr[j]
                            arr[j] = temp
                            j  = j*2
                        else:
                            break
                else:
                    continue




        self.heapList = arr
    
    def add(self, val: int) -> int:

        if (len(self.heapList)-1) < self.largest:
                self.heapList.append(val)
                e = len(self.heapList) - 1
                #procolate up
                while e > 1 and self.heapList[e] < self.heapList[e//2]:
                    temp = self.heapList[e//2]
                    self.heapList[e//2] = self.heapList[e]
                    self.heapList[e] = temp
                    e = e//2
        else:
            #check if current num is bigger than minimum of min heap
            if val > self.heapList[1]:
                #change the minimum of the min heap too the curr num
                j = 1
                self.heapList[j] = val
                #procalate down
                while (j*2) < len(self.heapList):
                    if j*2+1 < len(self.heapList) and self.heapList[j] > self.heapList[j*2+1] and self.heapList[j*2+1] < self.heapList[j*2]:
                        temp = self.heapList[j*2+1]
                        self.heapList[j*2+1] = self.heapList[j]
                        self.heapList[j] = temp
                        j  = j*2+1
                    elif self.heapList[j] > self.heapList[j*2]:
                        temp = self.heapList[j*2]
                        self.heapList[j*2] = self.heapList[j]
                        self.heapList[j] = temp
                        j  = j*2
                    else:
                        break

        return self.heapList[1]







        
