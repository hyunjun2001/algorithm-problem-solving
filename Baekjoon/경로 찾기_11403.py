# 백준 경로 찾기 문제이다.
# 문제 번호는 11403번이다.

import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input().strip())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 1:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=" ")
    print()
