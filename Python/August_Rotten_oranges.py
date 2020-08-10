class Solution:
    def orangesRotting(self, grid):
        rotten = []
        r, c, fresh, t = len(grid), len(grid[0]), 0, 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2: rotten.append([i, j])
                elif grid[i][j] == 1: fresh += 1
        
        while len(rotten) > 0:
            num = len(rotten)
            for i in range(num):
                x, y = rotten[0]
                rotten.pop(0)
                if x > 0 and grid[x-1][y] == 1: grid[x-1][y] = 2; fresh -= 1; rotten.append([x-1, y])
                if y > 0 and grid[x][y-1] == 1: grid[x][y-1] = 2; fresh -= 1; rotten.append([x, y-1])
                if x < r-1 and grid[x+1][y] == 1: grid[x+1][y] = 2; fresh -= 1; rotten.append([x+1, y])
                if y < c-1 and grid[x][y+1] == 1: grid[x][y+1] = 2; fresh -= 1; rotten.append([x, y+1])
            if len(rotten) > 0: t += 1
        
        return t if (fresh == 0) else -1

    '''Solution - 2
    from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1
        '''
        ''' Method -3 using deque
        class Solution(object):
    def orangesRotting(self, grid):
        n,m = len(grid), len(grid[0])
        Q = collections.deque([])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: cnt += 1
                if grid[i][j] == 2: Q.append((i,j))
        res = 0
        while Q:
            for _ in range(len(Q)):
                i,j = Q.popleft()
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=x<n and 0<=y<m and grid[x][y] == 1:
                        grid[x][y] = 2
                        cnt -= 1
                        Q.append((x,y))
            res += 1
        return max(0, res-1) if cnt == 0 else -1
        '''

if __name__=="__main__":
    grid=[[2,1,1],[1,1,0],[0,1,1]]
    c=Solution()
    print(c.orangesRotting(grid))
    
    