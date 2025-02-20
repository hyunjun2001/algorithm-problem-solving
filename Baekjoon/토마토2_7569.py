# 백준 토마토 문제이다.
# 문제 번호는 7569번

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]



def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if graph[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                    visited[nz][ny][nx] = True
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append((nz,ny, nx))


M, N, H = map(int, input().split())

queue = deque()
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
ans = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

bfs()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            ans = max(ans, graph[i][j][k])

print(ans - 1)
