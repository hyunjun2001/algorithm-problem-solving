# 백준 회의실 배정 문제입니다.
# 문제 번호는 1931번

import sys

input = sys.stdin.readline

n = int(input().strip())

table = []

for i in range(n):
    s, e = map(int, input().split())
    table.append((s, e))

table.sort(key=lambda x: (x[1], x[0]))
# print(table)

end = -1
ans = 0

for i in range(n):
    if table[i][0] >= end:
        end = table[i][1]
        ans += 1

print(ans)