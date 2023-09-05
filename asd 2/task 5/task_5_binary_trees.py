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

