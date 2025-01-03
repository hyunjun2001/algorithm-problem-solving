# 백준 헌내기는 친구가 필요해 문제이다.
# 문제 번호는 21736번

# dfs로 접근하니까 시간 초과가 난다...

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(i, j):
    global ans
    visited[i][j] = True
    if A[i][j] == 'P':
        ans += 1
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < N and 0 <= y < M and not visited[x][y]:
            if A[x][y] != 'X':
                dfs(x, y)


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
A = []

for _ in range(N):
    A.append(list(input().strip()))

visited = [[False] * M for _ in range(N)]
ans = 0

for i in range(N):
    if 'I' in A[i]:
        start_node = (i, A[i].index('I'))
        break

dfs(start_node[0], start_node[1])

if ans != 0:
    print(ans)
else:
    print('TT')


# bfs로 다시 풀기

import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j):
    global ans
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 <= x < N and 0 <= y < M:
                if A[x][y] != 'X' and not visited[x][y]:
                    queue.append((x, y))
                    visited[x][y] = True

                    if A[x][y] == 'P':
                        ans += 1


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
A = []

for _ in range(N):
    A.append(list(input().strip()))

visited = [[False] * M for _ in range(N)]
ans = 0

for i in range(N):
    if 'I' in A[i]:
        start_node = (i, A[i].index('I'))
        break

bfs(start_node[0], start_node[1])

if ans != 0:
    print(ans)
else:
    print('TT')
