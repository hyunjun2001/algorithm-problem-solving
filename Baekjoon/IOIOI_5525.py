# 백준 IOIOI 문제이다.
# 문제 번호는 5525번.

# https://devum.tistory.com/87 풀이 참조

import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
S = input().strip()

cur = 0
count = 0
ans = 0

while cur < (M-1):
    if S[cur:cur+3] == 'IOI':
        count += 1
        cur += 2
        if count == N:
            count -= 1
            ans += 1
    else:
        count = 0
        cur += 1

print(ans)

