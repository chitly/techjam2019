def solution(A):
    if len(A) == 0:
        return 0
    n_dup_cur = 1
    cur, before = A[0], None
    pair = [1, 0] # [n_cur, n_before]
    max_bi_valued_length = 1
    for i in range(1, len(A)):
        if A[i] == cur:
            n_dup_cur += 1
            pair[0] += 1
        elif A[i] == before:
            before, cur = cur, before
            pair = [pair[1] + 1, pair[0]]
            n_dup_cur = 1
        else:
            before, cur = cur, A[i]
            pair = [1, n_dup_cur]
            n_dup_cur = 1
        if pair[0] + pair[1] > max_bi_valued_length:
            max_bi_valued_length = pair[0] + pair[1]
    return max_bi_valued_length