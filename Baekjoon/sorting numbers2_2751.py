# 백준 수 정렬하기 2 문제이다.
# 문제 번호는 2751번
# 병합 정렬로 접근하자

import sys
input = sys.stdin.readline


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged_arr = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    merged_arr += left[l:]
    merged_arr += right[r:]
    return merged_arr


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr = merge_sort(arr)

for i in arr:
    print(i)
