# 백준 케빈 베이컨의 6단계 법칙 문제이다.
# 문제 번호는 1389번.

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

