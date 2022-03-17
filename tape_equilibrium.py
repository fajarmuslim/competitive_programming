def solution(A):
    
    sum_right = sum(A) - A[0]
    list_of_diff = []
    sum_left = A[0]
    

    for idx in range(1, len(A)-1):
        list_of_diff.append(abs(sum_left - sum_right))
        
        sum_left += A[idx]
        sum_right -= A[idx]
    
    list_of_diff.append(abs(sum_left - sum_right))
    
    return min(list_of_diff)