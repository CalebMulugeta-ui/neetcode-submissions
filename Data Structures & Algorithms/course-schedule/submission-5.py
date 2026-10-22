class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adjList = {i:[] for i in range(numCourses)}
        for crs,preq in prerequisites:
            adjList[crs].append(preq)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if adjList[crs] == []:
                return True

            visited.add(crs)
            for preq in adjList[crs]:
                if not dfs(preq):
                    return False
            visited.remove(crs)
            adjList[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True




        