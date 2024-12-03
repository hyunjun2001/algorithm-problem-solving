# 백준 소트 인사이드 문제이다.
# 문제 번호는 1427번

import sys
input = sys.stdin.readline

arr = list(map(int, str(input().strip())))

for i in range(0, len(arr)):
    max_index = i
    for j in range(i, len(arr)):
        if arr[j] > arr[max_index]:
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]

for i in arr:
    print(i, end="")
