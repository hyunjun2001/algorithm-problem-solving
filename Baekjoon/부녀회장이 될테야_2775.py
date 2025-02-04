# 백준 부녀회장이 퇼테야 문제이다.
# 문제 번호는 2775번

import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    floor = int(input().strip())
    ho = int(input().strip())
    data = [i for i in range(1, ho+1)]
    for i in range(floor):
        for j in range(1, ho):
            data[j] += data[j-1]
    print(data[-1])