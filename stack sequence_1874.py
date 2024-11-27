# 백준 알고리즘 문제풀이 스택 수열 문제이다.
# 백준 문제번호 1874번

# 수열, 자연수, 스택에서 나오는 수 이렇게 세 가지를 고려해야 한다.

import sys
input = sys.stdin.readline

N = int(input())  # 수열 수
A = []

for i in range(N):
    temp = int(input())
    A.append(temp)

stack = []
num = 1
result = True
ans = ""

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            ans += "+\n"
        stack.pop()
        ans += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            ans += "-\n"

if result:
    print(ans)
