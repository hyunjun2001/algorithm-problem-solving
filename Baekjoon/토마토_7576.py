# 백준 토마토 문제이다.
# 문제 번호는 7576번

import sys
from collections import deque

input =  sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx]==0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny,nx])


M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
ans = 0


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])

bfs()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans, graph[i][j])

print(ans-1)
