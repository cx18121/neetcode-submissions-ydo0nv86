class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        def add(r, c, dist):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            elif grid[r][c] != 2147483647:
                return
            else:
                grid[r][c] = dist + 1
                q.append((r, c))

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            r, c = q.popleft()
            dist = grid[r][c]
            for d in dirs:
                add(r + d[0], c + d[1], dist)
        
        return

