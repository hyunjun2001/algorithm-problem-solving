# 백준 알고리즘 문제풀이 구간합 구하기5 문제이다.
# 백준 문제번호 11660
# 변수 명을 길게 잡으면 메모리 초과가 뜬다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n + 1)]  # 원본 배열
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
