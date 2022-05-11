# 14178. 1차원 정원, D3

t = int(input())

for test_case in range(1, t+1):
    N, D = map(int, input().split())

    range = D * 2 + 1

    if N % range == 0:
        answer = N // range
    else:
        answer = N // range + 1

    print(f"#{test_case}",answer)


