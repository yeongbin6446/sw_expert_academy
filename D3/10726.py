# 10726. 이진수 표현, D3

t = int(input())

for tc in range(1 , t+1):
    N, M = map(int, input().split())
    cnt = 0
    binary = format(M,'b')
    binary = list(binary)
    if len(binary) > 30:
        binary = binary[:30]
    binary.reverse()

    for i in binary[:N]:
        if i == '1':
            cnt += 1

    print(f"#{tc}", end=' ')
    if cnt == N:
        print("ON")
    else:
        print('OFF')
