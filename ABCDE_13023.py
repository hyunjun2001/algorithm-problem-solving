# 백준 ABCDE 문제이다.
# 문제 번호 13023번

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False] * (n+1)
graph = [[] for _ in range(n)]
arrive = False

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


def dfs(start_node, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[start_node] = True
    for i in graph[start_node]:
        if not visited[i]:
            dfs(i, depth + 1)
    visited[start_node] = False


for i in range(n):
    dfs(i, 1)
    if arrive :
        break
for i in visited:
    if not i:
        ans = 0
        break

if arrive:
    print(1)
else:
    print(0)