def summ_digit_of_number(num: int) -> int:
    if num == 1:
        return 1
    if num < 1:
        return 0
    print(num)
    return summ_digit_of_number(num//10) + num%10


print(summ_digit_of_number(1990042))
