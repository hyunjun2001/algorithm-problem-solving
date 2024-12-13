# 백준 기타 레슨 문제이다.
# 문제 번호는 2343
# 주어진 배열을 어디서 끊을지 접근하는 게 아니라 저장소 크기를 어디서 끊을지를 이진탐색으로 접근

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0
    count = 0
    for i in arr:
        if total + i > mid:
            total = 0
            count += 1
        total += i
    if total != 0:
        count += 1
    if count > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)
