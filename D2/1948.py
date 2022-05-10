# 1948. 날짜 계산기, D2

t = int(input())

for test_case in range(1, t+1):

    m1, d1, m2, d2 = map(int, input().split())

    d = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    print(f"#{test_case}", end=' ')
    if m1 == m2:
        print(d2-d1+1)
    else:
        result = d[m1] - d1 + 1
        for i in range(m1+1, m2):
            result += d[i]
        result += d2
        print(result)
