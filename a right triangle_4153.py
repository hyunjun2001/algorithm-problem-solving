# 백준 직각삼각형 문제이다.
# 문제 번호는 4153번

import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    else:
        if arr[2] ** 2 == (arr[0] ** 2 + arr[1] ** 2):
            print("right")
        else:
            print("wrong")
