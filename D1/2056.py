# 2056. 연월일 달력, D1

t = int(input())

for i in range(t):
    ymd = input()
    y = ymd[:4]
    m = ymd[4:6]
    d = ymd[6:8]
    print(f"#{i+1}", end = ' ')
    if int(y) == 0:
        print(-1)
        continue
    else:
        if int(m) == 0 or int(m) > 12:
            print(-1)
            continue
        else:
            if int(m) == 2:
                if int(d) > 28 or int(d) == 0:
                    print(-1)
                    continue
            elif int(m) == 4 or 6 or 9 or 11:
                if int(d) > 30 or int(d) == 0:
                    print(-1)
                    continue
            else:
                if int(d) > 31 or int(d) == 0:
                    print(-1)
                    continue
            result = y + '/' + m + '/' + d
            print(result)





