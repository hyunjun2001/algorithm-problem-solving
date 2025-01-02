# 백준 듣보잡 문제이다.
# 문제 번호는 1764번

import sys
input = sys.stdin.readline

arr1 = []
arr2 = []
ans = []

n, m = map(int, input().split())

for i in range(n):
    arr1.append(input().strip())

for i in range(m):
    arr2.append(input().strip())

ans = list(set(arr1) & set(arr2))
ans.sort()

print(len(ans))
for i in ans:
    print(i)


# 딕셔너리를 이용해 풀면 어떨까?

import sys
input = sys.stdin.readline

arr = {}
ans = []

n, m = map(int, input().split())

for i in range(n):
    x = input().strip()
    arr[x] = i

for i in range(m):
    temp = input().strip()
    if temp in arr:
        ans.append(temp)

ans.sort()

print(len(ans))
for i in ans:
    print(i)