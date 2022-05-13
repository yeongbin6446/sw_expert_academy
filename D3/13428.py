# 13428. 숫자 조작, D3

t = int(input())

for test_case in range(1, t+1):
    N = int(input())
    min_val = N
    max_val = N
    N = list(str(N))

    for i in range(len(N)-1):
        for j in range(i+1, len(N)):
            N[i], N[j] = N[j], N[i]
            if N[0] != '0' and int(''.join(N)) < min_val:
                min_val = int(''.join(N))
            if N[0] != '0' and int(''.join(N)) > max_val:
                max_val = int(''.join(N))
            N[j], N[i] = N[i], N[j]

    print(f"#{test_case} {min_val} {max_val}")








    


