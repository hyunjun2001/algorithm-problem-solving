# 백준 적록색약 문제이다.
# 문제 번호는 10026

import sys
import copy
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y, visited, graph):
    color = graph[x][y]
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if (0 <= x + dx[i] < N) and (0 <= y + dy[i] < N):
                nx = x + dx[i]
                ny = y + dy[i]
                if not visited[nx][ny] and graph[nx][ny] == color:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


N = int(input())

graph_RGB = []
graph_RB = []
visited_RGB = [[False] * N for _ in range(N)]
visited_RB = [[False] * N for _ in range(N)]

ans_RGB = 0
ans_RB = 0

for i in range(N):
    graph_RGB.append(list(input().strip()))

graph_RB = copy.deepcopy(graph_RGB)

for i in range(N):
    for j in range(N):
        if graph_RB[i][j] == 'G':
            graph_RB[i][j] = 'R'

# 일반 케이스
for i in range(N):
    for j in range(N):
        if not visited_RGB[i][j]:
            ans_RGB += 1
            bfs(i, j, visited_RGB, graph_RGB)


# 적록색약 케이스
for i in range(N):
    for j in range(N):
        if not visited_RB[i][j]:
            ans_RB += 1
            bfs(i, j, visited_RB, graph_RB)

print(ans_RGB)
print(ans_RB)
