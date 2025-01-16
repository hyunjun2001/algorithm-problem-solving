# 백준 최소비용 구하기 문제입니다.
# 문제 번호는 1916번

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


N = int(input().strip())
M = int(input().strip())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])

