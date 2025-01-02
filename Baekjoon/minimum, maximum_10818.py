# 백준 최대, 최소 문제이다.
# 문제 번호는 10818번

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

print(min(arr), max(arr))
