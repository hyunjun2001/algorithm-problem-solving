# 백준 문자열 집합 문제이다.
# 문제 번호는 14425번.

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
word_list = set()
ans = 0

for _ in range(N):
    word_list.add(input().strip())

for _ in range(M):
    temp = input().strip()
    if temp in word_list:
        ans += 1

print(ans)
