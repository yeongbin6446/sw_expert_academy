# 2047. 신문 헤드라인, D1

headline = input()

for i in headline:
    if i.isalpha():
        print(i.upper(),end='')
    else:
        print(i,end = '')
