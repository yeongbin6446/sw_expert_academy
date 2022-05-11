# 1288. 새로운 불면증 치료법, D2

t = int(input())

for test_case in range(1, t+1):
    num = [False] * 10

    N = input()
    a = list(N)
    cnt = 2
    while True:


        for i in a:
            num[int(i)] = True

        a = int(N) * cnt
        a = list(str(a))

        if False not in num:
            break

        cnt += 1



    print(f"#{test_case} {int(''.join(a))-int(N)}")