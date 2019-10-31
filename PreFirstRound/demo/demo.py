def solution(A):
    sortedA = sorted(A)
    outA = 0
    for x in sortedA:
        if x < 1:
            continue
        elif outA == x - 1 or outA == x:
            outA = x
        else:
            return outA + 1
    return outA + 1