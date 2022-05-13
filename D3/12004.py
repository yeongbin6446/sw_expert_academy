# 12004. 구구단 1, D3

t = int(input())

for test_case in range(1, t+1):
    N = int(input())

    flag = False

    a = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

    for i in range(1, 10):
        if (N / i) in a:
            flag = True
            break
        else:
            flag = False

    print(f"#{test_case}",end=' ')
    if flag:
        print('Yes')
    else:
        print('No')
