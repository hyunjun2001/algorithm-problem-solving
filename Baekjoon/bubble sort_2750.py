# 백준 버블 소트 문제이다.
# 문제 번호는 1377번

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

for i in range(0, n, 1):
    changed = False
    for j in range(0, n - i - 1, 1):
        if arr[j] > arr[j+1]:
            changed = True
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    if not changed:
        print(i + 1)
        break


# 위 방식으로 풀면 시간초과로 틀린다.
# 핵심은 내부 for문이 몇 번 수행됐냐를 찾는거다.
# 근데 오른쪽으로 가는건 그냥 배열 쭉 끝까지 갈 수 있지만,
# 왼쪽 이동은 한 번만 가능하다.
# 따라서 왼쪽으로 어떤 수가 n번 이동했으면 for문이 n번 돌았다는 뜻이 된다.

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append((int(input()), i))

Max = 0
arr_sorted = sorted(arr)

for i in range(n):
    if Max < arr_sorted[i][1] - i:
        Max = arr_sorted[i][1] - i

print(Max + 1)
