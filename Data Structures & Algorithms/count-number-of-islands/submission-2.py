class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[-1] * len(grid[0]) for i in range(len(grid))]

        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if grid[r][c] == "1" and visited[r][c] == -1:
                visited[r][c] = 1
                if c < cols - 1:
                    dfs(r, c + 1)
                if r < rows - 1:
                    dfs(r + 1, c)
                if c > 0:
                    dfs(r, c - 1)
                if r > 0:
                    dfs(r - 1, c)
        
        ct = 0

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == "1" and visited[r][c] == -1:
                    dfs(r, c)
                    ct +=1

        return ct
                