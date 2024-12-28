# 백준 잃어버린 괄호 문제입니다.
# 문제 번호는 1541번

import sys
input = sys.stdin.readline

arr = list(map(str, input().strip().split('-')))
ans = 0


def summation(i):
    total = 0
    temp = str(i).split('+')
    for i in temp:
        total += int(i)
    return total


for i in range(len(arr)):
    temp = summation(arr[i])
    if i == 0:
        ans += temp
    else:
        ans -= temp

print(ans)