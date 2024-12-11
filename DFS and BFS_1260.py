# 백준 DFS와 BFS 문제이다.
# 문제 번호는 1260번.

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())  # 정점, 간선, 시작 노드
graph = [[] for _ in range(n+1)]

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n+1):
    graph[i].sort()

dfs_ans = []
bfs_ans = []


def dfs(start_node):
    visited[start_node] = True
    dfs_ans.append(start_node)

    for j in graph[start_node]:
        if not visited[j]:
            dfs(j)


def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        temp = queue.popleft()
        bfs_ans.append(temp)
        for k in graph[temp]:
            if not visited[k]:
                visited[k] = True
                queue.append(k)


visited = [False] * (n+1)
dfs(v)

visited = [False] * (n+1)
bfs(v)

for i in dfs_ans:
    print(i, end=" ")
print()
for i in bfs_ans:
    print(i, end=" ")
