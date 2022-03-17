def solution(A):
    dict_A = {}

    for num in A:
        dict_A[num] = 1
    
    for idx in range(1, len(A)+2):
        if idx not in dict_A:
            return idx