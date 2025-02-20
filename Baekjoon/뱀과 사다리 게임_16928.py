# 백준 뱀과 사다리 게임 문제이다.
# 문저 번호는 16928번

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_num):
    queue = deque([start_num])
    while queue:
        now = queue.popleft()
        if now == 100:
            print(graph[100])
            break
        for i in range(1, 7):
            next = now + i
            if 1 <= next < 101:
                if next in ladder.keys():
                    next = ladder[next]
                if next in snake.keys():
                    next = snake[next]
                if graph[next] == 0:
                    graph[next] = graph[now] + 1
                    queue.append(next)


graph = [0] * 101
N, M = map(int, input().split())
ladder = dict()
snake = dict()

for i in range(N):
    start, end = map(int, input().split())
    ladder[start] = end

for i in range(M):
    start, end = map(int, input().split())
    snake[start] = end


bfs(1)
