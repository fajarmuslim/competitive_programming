def solution(A):

    A_dict = {}

    for num in A:
        A_dict[num] = 1
    
    for num in range(1,len(A)+1):
        if num not in A_dict:
            return 0
    
    return 1