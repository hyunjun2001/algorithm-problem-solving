# 백준 숨바꼭질 문제이다.
# 문제 번호는 1697번

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_node):
    queue = deque([start_node])
    while queue:
        now = queue.popleft()
        if now == K:
            print(visited[now])
            break
        for i in (now - 1, now + 1, now * 2):
            if 0 <= i <= 10 ** 5 and not visited[i]:
                visited[i] = visited[now] + 1
                queue.append(i)


N, K = map(int, input().split())
visited = [0] * (10 ** 5 + 1)

bfs(N)
