arr = [50, 25, 75, 13, 35, 65, 85, 0, 18, 30, 45, 60, 70, 80, 90]

'''def GenerateBBSTArray(a: []) -> []:
    if not a:
        return []
    a.sort()
    print('a before: ', a)
    final_arr = [None] * len(a)
    index_center = (len(a) // 2)
    final_arr[0] = a.pop(index_center)
    i = 0
    while a:
        print('a: ', a)
        print('len: ', len(a))
        print('final arr: ', final_arr)
        left_index = len(a[:index_center])//2
        print('li: ', left_index)
        final_arr[i * 2 + 1] = a.pop(left_index)
        right_index = (len(a[index_center:])//2) + index_center
        print('iii: ', i * 2 + 2)
        print('ri: ', right_index)
        final_arr[i * 2 + 2] = a.pop(right_index)

        print('i:', i)
        i += 1

    return final_arr'''


def GenerateBBSTArray(a: []) -> []:

    length = len(a)
    summ_arr = [None]*length
    if length > 1:
        summ_arr[0] = a[length//2]
        #print('length//2: ', a[length//2])
        summ_arr[0 * 2 + 1] = GenerateBBSTArray(a[:length//2])
        summ_arr[0 * 2 + 2] = GenerateBBSTArray(a[1+(length//2):])
        #print('fin')
        return summ_arr
    elif length == 1:
        #print('[a]', a[0])
        return a[0]
    return None

'''def GenerateBBSTArray(a: []) -> []:
    summ_arr = [None]*len(a)
    start_ind = 0

    print('start_ind*2+1: ', start_ind * 2 + 2)
    if not a:
        return []
    summ_arr[start_ind] = a[len(a)//2]
    print(len(a) // 2)
    summ_arr[start_ind*2+1] = GenerateBBSTArray(a[:len(a)//2])
    summ_arr[start_ind * 2 + 2] = GenerateBBSTArray(a[1+len(a)//2:])
    return summ_arr'''






# print(arr)

arr.sort()
#print(arr)
new_arr = GenerateBBSTArray(arr)
print('final: ', new_arr)
#print('len: ', len(new_arr))
