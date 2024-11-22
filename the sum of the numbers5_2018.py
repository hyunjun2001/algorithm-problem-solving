# 백준 수들의 합5 문제이다.
# 문제 번호는 2018번.

# 부분합으로 접근해서 풀었더니 메모리 초과

import sys
input = sys.stdin.readline

N = int(input())

D = [0]
temp = 0
ans = 0

for i in range(1,N+1,1):
    temp += i
    D.append(temp)

for i in range(len(D)-1, 1, -1):
    for j in range(0, i, 1):
        if D[i] - D[j] == N:
            ans += 1

print(ans)


# 투포인터로 접근해서 해결 시도

import sys
input = sys.stdin.readline

N = int(input())

start_index = 1
end_index = 1
sum = 1
ans = 1

while end_index != N:
    if sum == N:
        ans += 1
        end_index += 1
        sum += end_index
    elif sum > N:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(ans)