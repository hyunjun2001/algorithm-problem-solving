# 백준 수 찾기 문제이다.
# 문제 번호는 1920번

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
nums = list(map(int, input().split()))


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in nums:
    print(binary_search(i, arr))

# 집합으로?
# 집합 접근이 3배 가까이 빠르다.

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
arr_2 = list(map(int, input().split()))

arr = set(arr)

for i in arr_2:
    if i in arr:
        print(1)
    else:
        print(0)