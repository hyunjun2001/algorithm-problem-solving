# 백준 단어 정렬 문제이다.
# 문제 번호는 1181번

import sys
input = sys.stdin.readline

n = int(input())
words = []

for i in range(n):
    temp = input().strip()
    if temp not in words:
        words.append(temp)

# 증복 제거
# words = list(set(words))

# 정렬
words.sort()
words.sort(key=len)

for i in words:
    print(i)