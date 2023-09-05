arr = [50, 25, 75, 13, 35, 65, 85, 0, 18, 30, 45, 60, 70, 80, 90]

'''def GenerateBBSTArray(a: []) -> []:
    if not a:
        return []
    a.sort()
    print('a before: ', a)
    final_arr = [None] * len(a)
    index_center = (len(a) // 2)
    final_arr[0] = a[index_center]
    i = 0
    while a:
        print('a: ', a)
        print('len: ', len(a))
        print('final arr: ', final_arr)
        left_index = len(a[:index_center])//2 - i
        print('li: ', left_index)
        final_arr[i * 2 + 1] = a[left_index]
        right_index = (len(a[index_center:])//2) + index_center + i
        print('iii: ', i * 2 + 2)
        print('ri: ', right_index)
        final_arr[i * 2 + 2] = a[right_index]

        print('i:', i)
        i += 1

    return final_arr'''


'''def GenerateBBSTArray(a: [int]) -> [int]:

    length: int = len(a)
    middle: int = length//2
    summ_arr: [int] = [None]*length
    if length > 1:
        summ_arr[0] = a[length//2]
        #print('length//2: ', a[length//2])
        print(GenerateBBSTArray(a[:middle]))
        summ_arr[1] = GenerateBBSTArray(a[:middle])
        summ_arr[2] = GenerateBBSTArray(a[1+middle:])
        print('fin')
        return summ_arr
    elif length == 1:
        print('[a]', a)
        return a
    return None#best realis'''

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

'''def GenerateBBSTArray(a: [int]) -> [int]:
    mid = len(a)//2
    node = [a[mid], None, None]
    if len(a) > 1:

    elif len(a) == 1:
        return node
    return None'''


'''def GenerateBBSTArray(arr: [int]) -> [int]:


    if not arr:
        return [] #null
    node = []
    mid = len(arr) // 2
    root = [arr[mid]]
    #print(mid)
    #print('arr: ', arr)
    #print('arr[mid]', arr[mid])

    #print('GEner:' ,GenerateBBSTArray(arr[:mid]))
    right = GenerateBBSTArray(arr[mid + 1:])
    left = GenerateBBSTArray(arr[:mid])

    #elif len(arr) == 1:
        #print('n1: ', node[:1])
       # return arr
    node = root + left + right
    return node'''

'''def bstlist(arr, st, end):
    newlst = []
    if st > end:
        return []
    mid = st + (end-st)/2
    print(mid)
    # adding the root list
    node = [arr[int(mid)], None, None]

    # node.left = sortedArrayToBST(arr, start, mid-1);
    node[1] = bstlist(arr, st, mid - 1)

    # node.right = sortedArrayToBST(arr, mid+1, end);
    node[2] = bstlist(arr, mid + 1, end)

    return node'''


'''def bstlist(arr,start,end):
    if start > end:
        return [] #null
    mid = start + (end - start) // 2
    root = [arr[mid]]
    return root + bstlist(arr, start, mid - 1) + bstlist(arr, mid + 1, end)'''

def GenerateBBSTArray(a: [int]) -> [int]:
    i: int = 0
    a.sort()
    summ_arr: [int] = [None]*len(a)
    def recurGenerateBBSTArrayFunc(arr: [int], i: int, summ_arr) -> [int]:
        if not arr:
            return summ_arr
        mid: int = len(arr)//2
        summ_arr[i] = arr[mid]
        summ_arr = recurGenerateBBSTArrayFunc(arr[:mid], i*2+1, summ_arr)
        summ_arr = recurGenerateBBSTArrayFunc(arr[mid + 1:], i*2+2, summ_arr)
        return summ_arr
    return recurGenerateBBSTArrayFunc(a, i, summ_arr)


#arr.sort()
#print(GenerateBBSTArray(arr))
print(GenerateBBSTArray(arr))


#print(arr)


#print(arr)
#ew_arr = GenerateBBSTArray(arr, )
#print('final: ', new_arr)
#print('len: ', len(new_arr))

'''a = [1,2,3]
print(a)
a[0:1] = [4, 5]
print(a)'''
