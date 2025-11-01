import heapq

def path_finder(grid, start, end, blocked):
    n, m = len(grid), len(grid[0])
    blocked = set(blocked)
    
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)]

    def neighbours(x, y):
        res = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx+1, ny+1) not in blocked:
                res.append((nx, ny))
        return res

    sx, sy = start[0] - 1, start[1] - 1
    ex, ey = end[0] - 1, end[1] - 1

    dist = [[float('inf')] * m for _ in range(n)]
    dist[sx][sy] = 0
    pq = [(0, sx, sy)]

    while pq:
        cost, x, y = heapq.heappop(pq)
        if (x, y) == (ex, ey):
            return cost
        if cost > dist[x][y]:
            continue

        nb = neighbours(x, y)
        if not nb:
            continue

        max_val = max(grid[i][j] for i, j in nb)

        for nx, ny in nb:
            c = 0
            if grid[nx][ny] < max_val:
                c = max_val - grid[nx][ny]

            if grid[x][y] >= max_val:
                c = max(c, grid[x][y] + 1 - grid[nx][ny])

            new_cost = cost + c
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny))

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    k = int(input())
    blocked = [tuple(map(int, input().split())) for _ in range(k)]

    print(path_finder(grid, start, end, blocked))
