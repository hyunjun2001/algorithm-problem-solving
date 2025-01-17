# 백준 타임머신 문제이다.
# 문제 번호는 11657번.

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = []
distance = [INF] * (N+1)

for i in range(M):
    s, e, w = map(int, input().split())
    graph.append((s, e, w))


def bf(start_node):
    distance[start_node] = 0
    for i in range(N):
        for j in range(M):
            s = graph[j][0]
            e = graph[j][1]
            w = graph[j][2]
            if distance[s] != INF and distance[e] > distance[s] + w:
                distance[e] = distance[s] + w
                if i == N-1:
                    return True
    return False


ans = bf(1)

if ans:
    print(-1)
else:
    for i in distance[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)
