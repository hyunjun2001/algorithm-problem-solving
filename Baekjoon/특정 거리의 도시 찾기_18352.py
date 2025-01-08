# 백준 특정 거리의 도시 찾기 문제이다.
# 문제 번호는 18352번

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [0] * (N+1)
ans = []

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)


def bfs(start_node):
    global ans
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[now] + 1
                queue.append(i)


bfs(X)

for i in range(N+1):
    if distance[i] == K:
        ans.append(i)

if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
