# 백준 이친수 문제이다.
# 문제 번호는 2193번

import sys
input = sys.stdin.readline


N = int(input().strip())
D = [0] * (91)
D[1] = 1
D[2] = 1

for i in range(3, N+1):
    D[i] = D[i-1] + D[i-2]

print(D[N])