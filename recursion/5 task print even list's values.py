def print_even_lists_values(lst: [int]) -> None:
    if len(lst) == 0:
        return
    if lst[0]%2 == 0:
        print(lst.pop(0))
    else:
        lst.pop(0)
    print_even_lists_values(lst)

print_even_lists_values([0, 1,2,3,4,5,6,7,8])