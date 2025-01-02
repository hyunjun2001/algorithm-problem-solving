# 백준 DNA 비밀번호 문제이다.
# 문제 번호는 12891번.
# 슬라이딩 윈도우를 이용해 풀어야 하는데, 여기서 핵심은 배열을 매번 새로 짜는 것이 아니라 앞뒤로 변경되는 부분만 반영
# 위 방식을 통해 연산량을 줄여서 접근해야 한다.

import sys
input = sys.stdin.readline

S, P = map(int, input().split())
arr = list(input())
condition = list(map(int, input().split()))

start = 0
end = P

ans = 0

check = [0] * 4
check[0] = arr[start: end].count('A')
check[1] = arr[start: end].count('C')
check[2] = arr[start: end].count('G')
check[3] = arr[start: end].count('T')

while True:
    temp = 1
    for i in range(4):
        if check[i] < condition[i]:
            temp = 0
            break

    ans += temp

    if end >= S:
        break

    if arr[start] == "A":
        check[0] -= 1
    elif arr[start] == "C":
        check[1] -= 1
    elif arr[start] == "G":
        check[2] -= 1
    elif arr[start] == "T":
        check[3] -= 1
    start += 1

    if arr[end] == "A":
        check[0] += 1
    elif arr[end] == "C":
        check[1] += 1
    elif arr[end] == "G":
        check[2] += 1
    elif arr[end] == "T":
        check[3] += 1
    end += 1

print(ans)

