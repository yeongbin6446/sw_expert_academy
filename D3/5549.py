# 5549. 홀수일까 짝수일까, D3

t = int(input())

for tc in range(1, t+1):
    N = int(input())

    if N % 2 == 0:
        res = 'Even'
    else:
        res = 'Odd'

    print(f"#{tc} {res}")