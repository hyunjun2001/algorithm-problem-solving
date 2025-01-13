# 백준 여횅 가자 문제이다.
# 문제 번호는 1976번.

import sys
sys.setrecursionlimit(10000)
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


N = int(input().strip())
M = int(input().strip())
ans = True
parent = [i for i in range(N+1)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            union(i+1,j+1)

route = list(map(int, input().split()))

start = find(route[0])
for i in route[1:]:
    if find(i) != start:
        ans = False
        break

if ans:
    print("YES")
else:
    print("NO")
