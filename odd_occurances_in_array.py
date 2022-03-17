def solution(A):
    dict_A = {}

    for num in A:
        if num in dict_A:
            dict_A[num] += 1
        else:
            dict_A[num] = 1
    
    for num, occurances in dict_A.items():
        if occurances % 2 == 1:
            return num