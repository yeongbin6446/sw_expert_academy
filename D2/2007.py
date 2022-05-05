# 2007. 패턴 마디의 길이, D2

p = input()

f = p[0]

cnt = 1
for i in range(1,len(p)):
    if p[i] == f:
        if p[:i] == p[i:i+i]:
            print(i)
        else:
            continue


