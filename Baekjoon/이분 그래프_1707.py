# 백준 이분 그래프 문제이다.
# 문제 번호는 1707번.

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

K = int(input().strip())


def dfs(start_node):
    global IsCorrect
    visited[start_node] = True
    for i in graph[start_node]:
        if not visited[i]:
            check[i] = (check[start_node] + 1) % 2
            dfs(i)
        elif check[i] == check[start_node]:
            IsCorrect = False


for i in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    check = [0] * (V+1)
    IsCorrect = True

    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1, V+1):
        if IsCorrect:
            dfs(i)
        else:
            break

    if IsCorrect:
        print("YES")
    else:
        print("NO")
