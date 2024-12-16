# 백준 비밀번호 찾기 문제이다.
# 문제 번호는 17219333333333333

import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 전체 사이트 수, 찾으려는 사이트 수

dict = {}

for _ in range(n):
    site = list(map(str, input().split()))
    dict[site[0]] = site[1]

for _ in range(m):
    search = input().strip()
    temp = dict.get(search)
    print(temp)
