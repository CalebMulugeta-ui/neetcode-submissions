from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        queue = deque()
        largestSeq = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in mySet:
                if len(queue) > largestSeq:
                    largestSeq = len(queue)
                mySet.remove(queue.popleft())
                l+=1
            else:
                queue.append(s[r])
                mySet.add(s[r])
                r+=1         

        if len(mySet) > largestSeq:
            largestSeq = len(mySet)

        return largestSeq			
		

        