# 백준 집합의 표현 문제이다.
# 문제 번호는 1717번.

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    if o == 0:
        union(a, b)
