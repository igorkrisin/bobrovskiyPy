def main_func(lst: [object]) -> None:
    i=0
    print_even_lists_index(lst, i)


def print_even_lists_index(lst: [object], i) -> None:
    if i >= len(lst):
        return
    if i % 2 == 0:
        print(lst[i])
    print_even_lists_index(lst, i+1)

main_func([1,2,3,4,5,6,7])




