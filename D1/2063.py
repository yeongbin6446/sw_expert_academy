#2063. 중간값 찾기, D1

N = int(input())
scores = list(map(int, input().split()))
median = (len(scores) - 1) // 2
scores.sort()
print(scores[median])
