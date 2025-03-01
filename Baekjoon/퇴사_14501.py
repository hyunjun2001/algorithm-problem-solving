# 백준 퇴사 문제이다.
# 문제 번호는 14501번.

import sys
input = sys.stdin.readline


N = int(input().strip())
D = [0] * (N + 2)
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N+1):
    T[i], P[i] = map(int, input().strip().split())

for i in range(N, 0, -1):
    if i + T[i] > N+1:
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1], D[i+T[i]] + P[i])

print(D[1])