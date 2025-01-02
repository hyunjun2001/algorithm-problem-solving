# 백준 주몽 문제이다.
# 문제 번호는 1940번.

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))

arr.sort()

start_index = 0
end_index = N-1

ans = 0

while start_index < end_index:
    sum = arr[start_index] + arr[end_index]
    if sum == M:
        ans += 1
        start_index += 1
        end_index -= 1
    elif sum < M:
        start_index += 1
    else:
        end_index -= 1

print(ans)