class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for _ in range(n)]
        def dfs(i, j) -> None:
            vis[i][j] = 1
            if int(grid[i][j]) == 0:
                return
            if i+1 <= n-1 and vis[i+1][j] == 0:
                dfs(i+1, j)
            if j+1 <= m-1 and vis[i][j+1] == 0:
                dfs(i, j+1)
            if i-1 >= 0 and vis[i-1][j] == 0:
                dfs(i-1, j)
            if j-1 >= 0 and vis[i][j-1] == 0:
                dfs(i, j-1)
            return
        cnt = 0
        for i, vi in enumerate(grid):
            for j, vj in enumerate(grid[i]):
                if int(vj) == 1 and vis[i][j] == 0:
                    print("aaa", i, j)
                    cnt += 1
                    dfs(i, j)
                    print(vis)
        return cnt