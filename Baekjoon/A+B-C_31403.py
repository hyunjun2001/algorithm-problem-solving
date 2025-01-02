# 백준 A + B - C 문제이다.
# 문제 번호는 31403번

import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
C = int(input())

ans1 = (int(A) + int(B)) - C
ans2 = int(A+B) - C

print(ans1)
print(ans2)