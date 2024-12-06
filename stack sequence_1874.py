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


# 아래가 시간이 거의 1/20로 줄어드는 훨씬 나은 접근법이다.

# 연습장임다

import sys
input = sys.stdin.readline

n = int(input())

stack, ans, temp = [], [], True

top = 1

for _ in range(n):
    num = int(input())
    while top <= num:
        stack.append(top)
        ans.append('+')
        top += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        temp = False
        break

if temp:
    for i in ans:
        print(i)
else:
    print("NO")