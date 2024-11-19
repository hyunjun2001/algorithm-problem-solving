# 백준 알고리즘 문제풀이 구간합 구하기1 문제이다.
# 백준 문제번호 11659
import sys
input = sys.stdin.readline

length, repeat = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * length

s[0] = a[0]

for i in range(1, length):
    s[i] = s[i-1] + a[i]

for i in range(repeat):
    start, end = map(int, input().split())
    if start < 2:
        ans = s[end - 1]
    else:
        ans = s[end - 1] - s[start - 2]
    print(ans)

# 책에서 제시한 모범 답안

import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_num = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_num.append(temp)

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_num[e] - prefix_num[s-1])