# 백준 쉬운 최단거리 문제이다.
# 문제 번호는 14940번.

# a에서 b로 가는 최단거리가 3이면, b에서 a로 가는 최단거리도 3이다.

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(start_node):
    queue = deque([start_node])
    visited[start_node[0]][start_node[1]] = 0
    while queue:
        now = queue.popleft()
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            if 0 <= x < n and 0 <= y < m and visited[x][y] == -1:
                if graph[x][y] == 0:
                    visited[x][y] = 0
                if graph[x][y] == 1:
                    visited[x][y] = visited[now[0]][now[1]] + 1
                    queue.append((x,y))


n, m = map(int, input().split())
graph = []
visited = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs((i, j))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
