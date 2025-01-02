# 백준 좌표 압축 문제이다.
# 문제 번호는 18870번

import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
arr_2 = sorted(list(set(arr)))

dict = {arr_2[i] : i for i in range(len(arr_2))}

for i in arr:
    print(dict[i], end = " ")
 