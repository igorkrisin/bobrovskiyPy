def degree(N: int, M: int):
    if M == 0 and N == 0:
        return 0
    if M == 0:
        return 1
    return degree(N, M-1)*N


print(degree(10, 2))
