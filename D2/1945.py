# 1945. 간단한 소인수분해, D2

t = int(input())

for test_case in range(1, t+1):
    N = int(input())

    n = [2, 3, 5, 7, 11]

    i = 0
    cnt = 0
    print(f"#{test_case}", end = ' ')
    while i < 5:
        if N % n[i] == 0:
            N = N / n[i]
            cnt += 1
        else:
            print(cnt, end=' ')
            cnt = 0
            i += 1
    print()
