
arr = [50, 25, 75, 13, 35, 65, 85, 0, 18, 30, 45, 60, 70, 80, 90]

def GenerateBBSTArray(a: []) -> []:
    if not a:
        return []
    a.sort()
    print('a before: ', a)
    final_arr = [None] * len(a)
    index_center = int((len(a) - 1) / 2)
    final_arr[0] = a.pop(index_center)
    i = 0
    while a:
        print('a: ', a)
        print('len: ', len(a))
        print('final arr: ', final_arr)
        left_index = int(len(a)/4)
        print('li: ', left_index)
        final_arr[i * 2 + 1] = a.pop(left_index)
        right_index = int(len(a)/1.5)
        print('iii: ', i * 2 + 2)
        print('ri: ', right_index)
        final_arr[i * 2 + 2] = a.pop(right_index)

        print('i:', i)
        i += 1

    return final_arr





#print(arr)

arr.sort()
#print(arr)
new_arr = GenerateBBSTArray(arr)
print('final: ', new_arr)
print('len: ', len(new_arr))
