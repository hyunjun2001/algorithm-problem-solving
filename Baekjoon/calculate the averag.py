# 백준 알고리즘 문제풀이 평균 구하기 문제이다.
# 백준 문제번호 1546

# 내가 푼 풀이

subjects_num = int(input())
scores = list(map(int, input().split()))

highest_score = max(scores)

for i in range(subjects_num):
    scores[i] = (scores[i] * 100) / highest_score

ans = sum(scores) / subjects_num

print(ans)

# 책에서 제시한 모범 답안
# 여기서 핵심은 굳이 for문으로 하나하나 바꾸지 않고 한 번에 다 바꾼 것임.

n = int(input())
myList = list(map(int, input().split()))
mymax = max(myList)
sumList = sum(myList)
print(sumList * 100 / mymax / n)