# 5688. 세제곱근을 찾아라, D3

t = int(input())

for tc in range(1, t+1):
    N = int(input())

    r = round(N ** (1.0/3.0))
    result = -1
    for i in range(1, r+1):
        if i*i*i == N:
            result = i

    print(f"#{tc} {result}")