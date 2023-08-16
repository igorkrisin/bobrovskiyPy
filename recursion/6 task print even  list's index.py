def print_even_lists_index(lst: [object], i=0) -> None:
    if i >= len(lst):
        return
    if i % 2 == 0:
        print(lst[i])
    print_even_lists_index(lst, i+1)

print_even_lists_index([1,2,3,4,5,6,7])




