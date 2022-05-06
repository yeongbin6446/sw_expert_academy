# 1976. 시각 덧셈, D2

t = int(input())

for i in range(t):
    h1, m1, h2, m2 = map(int,input().split())

    if m1 + m2 > 59:
        result_m = (m1 + m2) - 60
        result_h = 1 + h1 + h2
        if result_h > 12:
            result_h = result_h - 12
    else:
        result_m = m1 + m2
        result_h = h1 + h2
        if result_h > 12:
            result_h = result_h - 12

    print(f"{i+1} {result_h} {result_m}")

