# 백준 연결 요소의 개수 문제이다.
# 문제 번호는 11724번

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())  # 정점 개수, 간선 개수
visited = [False] * (n + 1)
A = [[] for _ in range(n + 1)]

for i in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0


def dfs(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i)


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
