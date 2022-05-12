# 13229. 일요일, D3

t = int(input())

for test_case in range(1, t+1):
    arr = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    d = input()

    idx = arr.index(d)

    print(f"#{test_case}",end=' ')
    if 6 - idx == 0:
        print(7)
    else:
        print(6-idx)
