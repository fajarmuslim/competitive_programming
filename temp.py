def solution(N, A):
    
    def find_idx_of_N1(arr):
        res = []
        for (idx, num) in enumerate(arr):
            if num == N + 1:
                res.append(idx)
        
        return res

    idx_n_plus_1s = find_idx_of_N1(A)
    max_idx = max(idx_n_plus_1s)

    def get_max_occurances(arr):
        dict_arr = {}
        for num in arr:
            if num in dict_arr:
                dict_arr[num] += 1
            else:
                dict_arr[num] = 1

        return max(dict_arr.values())

    res = 0
    prev = 0
    for idx_n_plus_1 in idx_n_plus_1s:
        res += get_max_occurances(A[prev:idx_n_plus_1])
        prev = idx_n_plus_1

    result = [res for i in range(N)]
    for idx in range(max_idx, len(A)):
        result[A[idx]-1] += 1

    return result