# 1989. 초심자의 회문 검사, D2

t = int(input())

for i in range(t):
    words = input()

    words = list(words)
    temp = list(words)
    temp.reverse()
    print(f"#{i+1}",end = " ")
    if words == temp:
        print(1)
    else:
        print(0)