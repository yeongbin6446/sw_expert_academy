# 12221. 구구단2, D3

t = int(input())

for test_case in range(1, t+1):
    A, B = map(int, input().split())

    print(f"#{test_case}",end=' ')
    if A >= 10 or B >= 10:
        print(-1)
    else:
        print(A * B)