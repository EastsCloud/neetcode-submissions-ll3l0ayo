class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p = [[] for i in range(numCourses)]
        cy = True
        for i in prerequisites:
            p[i[0]].append(i[1])
        vis = [0 for i in range(numCourses)]
        def dfs(c) -> None:
            nonlocal cy
            vis[c] = 1
            for i in p[c]:
                if vis[i] == 0:
                    dfs(i)
                else:
                    cy = False
                    return
            vis[c] = 0
            return
        
        for i in range(numCourses):
            if vis[i] == 0:
                dfs(i)

        return cy
        