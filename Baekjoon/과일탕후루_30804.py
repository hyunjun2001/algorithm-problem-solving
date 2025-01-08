# 백준 과일탕후루 문제이다.
# 문제 번호는 30804번

# 처음으로 떠올린 풀인데 시간초과로 탈락

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

num = int(input().strip())
arr = list(map(int, input().split()))
ans = 0


def search(arr):
    global ans
    if len(list(set(arr))) <= 2:
        ans = max(ans, len(arr))
        return

    search(arr[:-1])
    search(arr[1:])


search(arr)
print(ans)


# 두 번쨰로 접근한 풀이
# 아래 사이트의 풀이를 참고해서 풀었습니다.
# https://velog.io/@ouk/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%B0%B1%EC%A4%80-%EB%B0%B1%EC%A4%80-30804%EB%B2%88-%EA%B3%BC%EC%9D%BC-%ED%83%95%ED%9B%84%EB%A3%A8-%EB%AC%B8%EC%A0%9C-Python%EC%9C%BC%EB%A1%9C-%EC%99%84%EB%B2%BD-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0

import sys
input = sys.stdin.readline

num = int(input().strip())
arr = list(map(int, input().split()))

count = {}
distinct_count = 0
ans = 0
left = 0

for right in range(num):
    if arr[right] not in count:
        count[arr[right]] = 1
        distinct_count += 1
    else:
        count[arr[right]] += 1

    while distinct_count > 2:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
            distinct_count -= 1
        left += 1

    ans = max(ans, right - left + 1)

print(ans)
