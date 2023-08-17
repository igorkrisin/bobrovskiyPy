def main_func(lst: [int]) -> None:
    i = 0
    print_even_lists_values(lst, i)
    


def print_even_lists_values(lst: [int], i=0) -> None:
    if i >= len(lst):
        return
    if lst[i] % 2 == 0:
        print(lst[i])
    print_even_lists_values(lst, i + 1)

main_func([0, 1, 2, 3, 4, 5, 6, 7, 16])
#print_even_lists_values([0, 1, 2, 3, 4, 5, 6, 7, 16])
