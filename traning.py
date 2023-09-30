def fact(n: int)->int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fact(n-1)*n



print(fact(5))

