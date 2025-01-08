# 백준 효율적인 해킹 문제이다.
# 문제 번호는 1325번

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = []

for i in range(M):
    s, e = map(int, input().split())
    graph[e].append(s)


def bfs(start_node):
    visited[start_node] = True
    queue = deque([start_node])
    cnt = 1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt


for i in range(1, N+1):
    visited = [False] * (N+1)
    ans.append(bfs(i))

max_cnt = max(ans)
for i in range(N):
    if ans[i] == max_cnt:
        print(i+1, end=' ')