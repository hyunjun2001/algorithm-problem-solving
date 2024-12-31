# 백준 패션왕 신해빈 문제이다.
# 문제 번호는 9375번

import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    cases = int(input().strip())
    clothes = {}
    for i in range(cases):
        temp = list(map(str, input().split()))
        if temp[1] not in clothes:
            clothes[temp[1]] = [temp[0]]
        else:
            clothes[temp[1]].append(temp[0])

    cnt = 1

    for i in clothes:
        cnt *= (len(clothes[i]) + 1)
    print(cnt - 1)

