def main_funct(lst: [int]) -> int:
    max_el = lst[0]
    sec_max_el = lst[1]
    i = 2
    return second_max_el_recursion(lst, max_el, sec_max_el, i)


def second_max_el_recursion(lst: [int], max_el, sec_max_el, i) -> int:
    if i >= len(lst):
        return sec_max_el
    if lst[i] > max_el:
        sec_max_el = max_el
        max_el = lst[i]
    elif lst[i] > sec_max_el:
        sec_max_el = lst[i]

    return second_max_el_recursion(lst, max_el, sec_max_el, i + 1)


print(main_funct([8, 7, 6, 3, 6]))
























def second_max_el_loop(lst: [int]) -> int:
    max_el = lst[0]
    sec_max_el = lst[1]
    for i in range(2, len(lst)):
        if lst[i] > max_el:
            sec_max_el = max_el
            max_el = lst[i]
        elif lst[i] > sec_max_el:
            sec_max_el = lst[i]
    print('max_el: ', max_el)
    return sec_max_el


#print('loop: ', second_max_el_loop([8, 7, 3, 6, 7]))
