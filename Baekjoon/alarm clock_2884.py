# 백준 알람 시계 문제이다.
# 문제 번호는 2884번

import sys
input = sys.stdin.readline

h, m = map(int, input().split())

if m >= 45:
    print(f"{h} {m-45}")
else:
    if h == 0:
        print(f"23 {60+(m-45)}")
    else:
        print(f"{h-1} {60+(m-45)}")
