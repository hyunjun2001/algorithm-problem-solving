# 백준 최소 스패닝 트리 문제이다.
# 문제 번호는 1197번.

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


V, E = map(int, input().split())
graph = []
parents = [i for i in range(V+1)]
ans = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append([C, A, B])

graph.sort()

for edge in graph:
    cost, s, e = edge
    if find(s) != find(e):
        union(s, e)
        ans += cost

print(ans)
