# 14363. 숫자가 같은 배수, D3

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    flag = False

    li = list(str(N))
    a = []
    for i in range(2,11):
        if len(list(str((N * i)))) == len(li):
            a.append(list(str(N*i)))

    print(f"#{tc}",end=' ')
    for i in a:
        for j in i:
            if j in li:
                flag = True
            else:
                flag = False
                break

        if flag:
            print("possible")
            break

    if not flag:
        print("impossible")
