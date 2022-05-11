# 1285. 아름이의 돌 던지기, D2

t = int(input())

for test_case in range(1, t+1):

    N = int(input())
    dif = []

    dis = list(map(int, input().split()))

    for i in dis:
        dif.append(abs(i - 0))

    m = min(dif)

    cnt = 0
    for i in dif:
        if m == i:
            cnt += 1

    print(f"#{test_case} {m} {cnt}")