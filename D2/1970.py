# 1970. 쉬운 거스름돈, D2

t = int(input())

m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in range(t):
    won = int(input())
    print(f"#{i+1}")
    for j in range(len(m)):
        a = won // m[j]
        if a != 0:
            won = won - (a * m[j])
        print(a , end = " ")
    print()


