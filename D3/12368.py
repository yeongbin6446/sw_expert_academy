# 12368. 24시간, D3

t = int(input())

for test_case in range(1, t+1):
    A, B = map(int, input().split())

    print(f"#{test_case}",end=' ')
    if A+B >= 24:
        print((A+B)-24)
    else:
        print(A+B)