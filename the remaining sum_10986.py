# 백준 알고리즘 문제풀이 나머지 합 문제이다.
# 백준 문제번호 10986

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = 0  # 정답 변수

A = list(map(int, input().split()))
A_remain = []

for i in A:
    A_remain.append(i % M)

D_remain = [0]  # 나머지들의 부분합
temp = 0

for i in A_remain:
    temp += i
    D_remain.append(temp)

for i in range(len(D_remain) - 1, 0, -1):
    for j in range(0, i):
        if (D_remain[i] - D_remain[j]) % M == 0:
            ans += 1

print(ans)


# 위 방식대로 풀면 답은 맞는데 시간 초과다.
# 시간을 줄이기 위해선 일단 합 자체가 0이 되는 애들을 더한다.
# 이후 나머지가 같은 애들 중에서 3C2로 빼주는 경우를 계산해야 한다.
# 이 방식대로 하면 2중 for문을 돌리지 않고 연산 횟수도 줄어들어 통과 가능.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * N
C = [0] * M

S[0] = A[0]
ans = 0

for i in range(1, N):
    S[i] = S[i-1] + A[i]

for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        ans += 1
    C[remainder] += 1

for i in range(M):
    if C[i] > 1:
        ans += (C[i] * (C[i] -1) // 2)

print(ans)
