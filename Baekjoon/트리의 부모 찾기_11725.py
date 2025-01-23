# 백준 트리의 부모 찾기 문제이다.
# 문제 번호는 11725번

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input().strip())
visited = [False] * (N+1)
tree = [[] for _ in range(N+1)]
ans = [0] * (N+1)

for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)


def dfs(start_node):
    visited[start_node] = True
    for node in tree[start_node]:
        if not visited[node]:
            ans[node] = start_node
            dfs(node)


dfs(1)

for i in ans[2:]:
    print(i)