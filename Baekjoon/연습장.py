import sys
input = sys.stdin.readline


N = int(input().strip())

D = [0] * 1001
mod = 10_007
D[1] = 1
D[2] = 2

for i in range(3, N + 1):
    D[i] = (D[i - 1] + D[i - 2]) % mod

print(D[N])
