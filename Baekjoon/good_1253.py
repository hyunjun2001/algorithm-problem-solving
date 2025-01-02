# 백준 좋다 문제이다.
# 문제 번호는 1253번.

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0

for i in range(N):
    find = arr[i]
    start_index = 0
    end_index = N - 1
    while start_index < end_index:
        sum = arr[start_index] + arr[end_index]
        if sum == find:
            if i != start_index and i != end_index:
                ans += 1
                break
            elif i == start_index:
                start_index += 1
            elif i == end_index:
                end_index -= 1
        elif sum < find:
            start_index += 1
        else:
            end_index -= 1

print(ans)
