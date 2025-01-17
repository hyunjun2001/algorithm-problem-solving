# 백준 케빈 베이컨의 6단계 법칙 문제이다.
# 문제 번호는 1389번.

# bfs 풀이

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = []

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                bacon[i] = bacon[now] + 1
                queue.append(i)


for i in range(1, N+1):
    visited = [False] * (N + 1)
    bacon = [0] * (N + 1)
    bfs(i)
    ans.append(sum(bacon))

temp = min(ans)

for i in range(N):
    if ans[i] == temp:
        print(i+1)
        break


# 플루이드 워셜 풀이

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

MIN = INF
ans = -1

for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp += graph[i][j]
    if MIN > temp:
        MIN = temp
        ans = i

print(ans)
