# 백준 카드2 문제이다.
# 문제 번호는 2164번

from collections import deque
import sys
input = sys.stdin.readline

queue = deque()

n = int(input())

for i in range(n):
    queue.appendleft(i + 1)

while len(queue) != 1:
    queue.pop()  # 가장 위에 숫자 버리기
    temp = queue.pop()  # 그 다음 위에 숫자는 제일 밑으로 보내기
    queue.appendleft(temp)

print(queue[0])
