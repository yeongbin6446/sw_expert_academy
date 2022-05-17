# 9700. USB 꽂기의 미스테리, D3

t = int(input())

for tc in range(1 , t+1):
    p, q = map(float, input().split())
    s1 = (1-p) * q
    s2 = p * (1-q) * q
    print(f"#{tc}",end=' ')
    if s1 > s2:
        print("NO")
    else:
        print("YES")