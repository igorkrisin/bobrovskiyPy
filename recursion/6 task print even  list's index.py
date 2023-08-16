def print_even_index_list(lst: [object]) -> None:
    if len(lst) == 0:
        return
    print(lst.pop(0))
    if len(lst) != 0:
        lst.pop(0)
        print_even_index_list(lst)


print_even_index_list([0, 1, 2])


