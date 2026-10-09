class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        myMap = defaultdict(list)

        for word in strs:
            alphaList = [0] * 26
            for char in word:
                indx = ord(char) - 97
                alphaList[indx] += 1
            tupleAlpha = tuple(alphaList)
            if tupleAlpha in myMap:
                myMap[tupleAlpha].append(word)
            else:
                myMap[tupleAlpha].append(word)

        
        res = []

        for i in myMap.values():
            res.append(i)
        
        return res
