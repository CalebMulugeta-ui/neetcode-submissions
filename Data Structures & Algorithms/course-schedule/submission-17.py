from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjMap = {}
        for src, dst in prerequisites:
            if src not in adjMap:
                adjMap[src] = []
            if dst not in adjMap:
                adjMap[dst] = []
            adjMap[src].append(dst)
        
        visit = set()
        def dfs(crs): 
            if crs in visit:
                return False

            if adjMap[crs] == []:
                return True 

            visit.add(crs)
            for preq in adjMap[crs]:
                if not dfs(preq):
                    return False
            
            visit.remove(crs)
            adjMap[crs] = []
            return True

        
        for crs in range(numCourses):
            if crs in adjMap:
                if not dfs(crs):
                    return False
        return True
           