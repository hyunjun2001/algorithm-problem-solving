# 백준 나이순 정렬 문제이다.
# 문제 번호는 10814번

import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    age, name = map(str, input().strip().split())
    age = int(age)
    arr.append([age, name])

arr.sort(key=lambda x: (x[0]))

for i, j in arr:
    print(f'{i} {j}')
