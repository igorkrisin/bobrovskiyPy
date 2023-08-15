def len_list(lst: [object]) -> int:
    if len(lst) == 0:
        return 0
    return len_list(lst[1:]) + 1


print(len_list([1, 2, 3, 4, 5, 'a', 'v']))
