# 백준 마인크래프트 문제이다.
# 문제 번호는 18111번

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
idx = 0

# print(arr)

for floor in range(257):
    exceed, lack = 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] > floor:
                exceed += arr[i][j] - floor
            else:
                lack += floor - arr[i][j]

    if exceed + B >= lack:
        if (exceed * 2) + lack <= ans:
            ans = (exceed * 2) + lack
            idx = floor

print(ans, idx)