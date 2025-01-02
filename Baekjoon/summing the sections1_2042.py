# 백준 알고리즘 문제풀이 구간합 구하기5 문제이다.
# 백준 문제번호 2042

# 음 이건 트리 개념이 필요해서 아직은 아니다.
# 임튼 트리 공부하고 재도전 예정

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

A = []

for i in range(N):
    num = int(input())
    A.append(num)

for i in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        A[b-1] = c
    if a == 2:
        D = [0]
        temp = 0
        for i in range(N):
            temp += A[i]
            D.append(temp)
        result = D[c] - D[b-1]
        print(result)
