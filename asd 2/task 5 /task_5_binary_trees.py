
arr = [50, 25, 75, 46, 37, 62, 84, 88, 20, 31, 43, 55, 51, 14, 92]


def GenerateBBSTArray(a: []) -> []:
    if not a:
        return []
    a.sort()
    final_arr = [None] * len(a)
    index_center = int((len(a) - 1) / 2)
    final_arr[0] = arr[index_center]
    i = 0
    while i < len(a)-5:


        print('final arr: ', final_arr)
        left_index = int(index_center/2)
        print('li: ', left_index)
        final_arr[i * 2 + 1] = arr[left_index]
        right_index = int(index_center + index_center/2)
        final_arr[i * 2 + 2] = arr[right_index]
        i += 1
        print(i)
    return final_arr





#print(arr)

arr.sort()
#print(arr)
GenerateBBSTArray(arr)