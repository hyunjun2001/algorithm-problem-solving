# 백준 카잉 달력 문제이다.
# 문제 번호는 6064번

T = int(input().strip())


def search(M, N, x, y):
    K = x
    while K <= M* N:
        if ((K - x) % M == 0) and ((K-y) % N == 0):
            return K
        else:
            K += M
    return -1


for i in range(T):
    M, N, x, y = map(int, input().strip().split())
    print(search(M, N, x, y))