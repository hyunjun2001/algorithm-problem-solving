# 백준 트리의 지금 문제이다.
# 문제 번호는 1167번

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())  # 노드 개수
graph = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index += 1
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index+1]
        graph[s].append((e, v))
        index += 2

distance = [0] * (n+1)
visited = [False] * (n+1)


def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i[0]]:
                queue.append(i[0])
                visited[i[0]] = True
                distance[i[0]] = i[1] + distance[node]


bfs(1)
maximum = 1

for i in range(2, n+1):
    if distance[maximum] < distance[i]:
        maximum = i

distance = [0] * (n+1)
visited = [False] * (n+1)

bfs(maximum)
print(max(distance))
