# 1204. 최빈수 구하기, D2

t = int(input())

for test_case in range(1, t+1):
    N = int(input())

    index = [0] * 101
    scores = list(map(int, input().split()))

    for i in scores:
        index[i] += 1

    m = max(index)

    for i in range(101):
        if m == index[i]:
            result = i

    print(f"#{test_case}",result)

