# 2029. 몫과 나머지 출력하기

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    print(f"#{t+1} {a // b} {a % b}")
