def second_max_el_recursion(lst: [int], max_el=0, sec_max_el=0, i=0) -> int:
    if i >= len(lst):
        return sec_max_el
    if lst[i] > max_el:
        sec_max_el = max_el
        max_el = lst[i]
    elif lst[i] > sec_max_el:
        sec_max_el = lst[i]

    return second_max_el_recursion(lst, max_el, sec_max_el, i + 1)


print(second_max_el_recursion([7, 6, 3, 6, 8]))


def second_max_el_loop(lst: [int]) -> int:
    max_el = 0
    sec_max_el = 0
    for i in range(0, len(lst)):
        if lst[i] > max_el:
            sec_max_el = max_el
            max_el = lst[i]
        elif lst[i] > sec_max_el:
            sec_max_el = lst[i]
    print('max_el: ', max_el)
    return sec_max_el


#print('loop: ', second_max_el_loop([1, 7, 3, 6, 7]))
