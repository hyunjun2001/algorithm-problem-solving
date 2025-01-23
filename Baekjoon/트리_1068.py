# 백준 트리 문제이다.
# 문제 번호는 1068번

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input().strip())
visited = [False] * (N)
tree = [[] for _ in range(N)]
ans = 0
p = list(map(int, input().split()))
delete = int(input().strip())

for i in range(N):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i


def dfs(start_node):
    global ans
    child = 0
    visited[start_node] = True
    for i in tree[start_node]:
        if not visited[i] and i != delete:
            child += 1
            dfs(i)
    if child == 0:
        ans += 1


if delete == root:
    print(0)
else:
    dfs(root)
    print(ans)