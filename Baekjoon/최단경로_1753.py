# 백준 최단경로 문제이다.
# 문제 번호는 1753번

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start_node):
    arr = []
    heapq.heappush(arr, (0, start_node))
    distance[start_node] = 0
    while arr:
        dist, now = heapq.heappop(arr)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(arr, (cost, i[0]))


V, E = map(int, input().split())
start_node = int(input().strip())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

dijkstra(start_node)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

