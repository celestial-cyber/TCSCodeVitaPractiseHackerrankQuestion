def bpm(u, seen, match_r, graph):
    for v in graph[u]:
        if not seen[v]:
            seen[v] = True
            if match_r[v] == -1 or bpm(match_r[v], seen, match_r, graph):
                match_r[v] = u
                return True
    return False

def min_cars_needed(races):
    n = len(races)
    races.sort(key=lambda x: x[2])
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, d1 = races[i]
            x2, y2, d2 = races[j]
            dist = abs(x2 - x1) + abs(y2 - y1)
            if d2 - d1 >= dist:
                graph[i].append(j)
    match_r = [-1] * n
    result = 0
    for i in range(n):
        seen = [False] * n
        if bpm(i, seen, match_r, graph):
            result += 1
    return n - result

if __name__ == "__main__":
    n = int(input())
    races = []
    for _ in range(n):
        x, y, d = map(int, input().split())
        races.append((x, y, d))
    print(min_cars_needed(races))
