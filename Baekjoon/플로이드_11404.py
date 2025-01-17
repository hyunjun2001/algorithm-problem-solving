# 백준 플로이드 문제이다.
# 문제 번호는 11404번

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().strip())
m = int(input().strip())

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    s, e, w = map(int, input().split())
    if graph[s][e] > w:
        graph[s][e] = w

for k in range(1, n + 1):  # 경유지 정보
    for i in range(1, n + 1):  # 출발지 정보
        for j in range(1, n + 1):  # 도착지 정보
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
