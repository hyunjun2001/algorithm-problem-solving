# 백준 알고리즘 문제풀이 숫자의 합 구하기 문제이다.
# 백준 문제번호 11720

num_count = int(input())
n_numbers = input()

ans = 0

for i in range(num_count):
    ans += int(n_numbers[i])

print(ans)