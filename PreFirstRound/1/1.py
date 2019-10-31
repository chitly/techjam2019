def solution(S):
    setOfAlphabet = set()
    numberOfSubString = 1
    for x in S:
        if x not in setOfAlphabet:
            setOfAlphabet.add(x)
        else:
            setOfAlphabet = { x }
            numberOfSubString += 1
    return numberOfSubString