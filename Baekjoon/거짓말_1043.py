# 백준 거짓말 문제이다.
# 문제 번호는 1043번

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


N, M = map(int, input().split())
A = list(map(int, input().split()))[1:]
party = []
parent = [i for i in range(N+1)]
count = 0

for i in range(M):
    temp = list(map(int, input().split()))[1:]
    party.append(temp)

for i in range(M):
    first = party[i][0]
    for j in range(1, len(party[i])):
        union(first, party[i][j])

for i in range(M):
    ans = True
    first = party[i][0]
    for j in range(len(A)):
        if find(first) == find(A[j]):
            ans = False
            break
    if ans:
        count += 1

print(count)