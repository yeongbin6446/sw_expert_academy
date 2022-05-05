# 1986. 지그재그 숫자, D2

t = int(input())

for i in range(t):
    N = int(input())

    result = 1
    for n in range(2, N+1):
        if n % 2 == 0:  #짝수
            result -= n
        else:   #홀수
            result += n
    print(f"f{i+1} {result}")
