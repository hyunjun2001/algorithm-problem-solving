# 백준 오큰수 문제이다.
# 문제 번호는 17298번

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = [-1] * n

for i in range(n):
    temp = n - 1
    while temp != i:
        if arr[temp] > arr[i]:
            ans[i] = arr[temp]
        temp -= 1

for i in ans:
    print(i, end=" ")



# 위 풀이가 가장 처음에 생각한 방식인데 시간초과로 틀렸다.
# 시간초과를 에방하기 위해선 스택으로 접근해야 한다.
# 스택에 인덱스를 넣고 빼는 방식으로 접근해야 하는데, 초깃값은 바로 스택에 인덱스 0을 넣는다.
# 이후 스택에 가장 위에 있는 숫자와 arr과 비교해 오큰수에 해당하지 않으면 걔도 스택에 넣고
# 해당하면 다 빼고 정답 값에 오큰수에 해당하는 수를 넣는다.

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n

stack = []

for i in range(0, n):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

for i in range(n):
    print(ans[i], end=" ")
