# 백준 K번째 수 문제이다.
# 문제 번호는 11004번

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, center, right = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            center.append(num)
    return quick_sort(left) + center + quick_sort(right)


arr = quick_sort(arr)
print(arr[k-1])


# 위 방식대로 하면 시간초과

n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

print(arr[k-1])