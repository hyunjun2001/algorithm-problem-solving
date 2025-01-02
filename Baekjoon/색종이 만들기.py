# 백준 색종이 만들기 문제이다.
# 문제 번호는 2630번

import sys
input = sys.stdin.readline

n = int(input().strip())
table = [list(map(int, input().split())) for _ in range(n)]

# print(table)

ans_0 = 0
ans_1 = 0


def search(x, y, n):
    global ans_0, ans_1
    color = table[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != table[i][j]:
                search(x, y, n//2)
                search(x+n//2, y, n//2)
                search(x, y+n//2, n//2)
                search(x+n//2, y+n//2, n//2)
                return

    if color == 0:
        ans_0 += 1
    elif color == 1:
        ans_1 += 1


search(0, 0, n)
print(ans_0)
print(ans_1)
