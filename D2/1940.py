# 1940. 가랏! RC카!, D2

t = int(input())

for test_case in range(1, t+1):
    N = int(input())
    speed = 0
    d = 0
    for i in range(N):
        command = input()

        if command == '0':
            pass
        else:
            a = int(command.split(' ')[0])
            b = int(command.split(' ')[1])

            if a == 1:
                speed += b

            if a == 2:
                if speed < b:
                    speed = 0
                else:
                    speed -= b


        d += speed
    print(f"#{test_case} {d}")