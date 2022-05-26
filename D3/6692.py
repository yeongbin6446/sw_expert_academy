# 6692. 다솔이의 월급 상자, D3

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    avg = 0
    for i in range(N):
        p, x = input().split()
        p, x = float(p), int(x)
        avg += p*x

    print(f"#{tc} {avg:.6f}")

