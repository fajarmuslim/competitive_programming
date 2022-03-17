def solution(X, Y, D):
    
    count_jump = 0
    if (Y - X) > 0:
        if (Y - X) % D == 0:
            count_jump = (Y-X) // D
        else:
            count_jump = ((Y-X) // D)+ 1

    return count_jump