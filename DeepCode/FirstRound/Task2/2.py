def printOut(p):
    print(len(p))
    for x in p:
        print(x)

def pushStack(x, stack, inStack, canUse):
    if x not in inStack:
        inStack.add(x)
        stack.append(x)
    else:
        while stack[-1] != x:
            canUse.remove(stack[-1])
            stack.pop()
        return True
    return False

def extendP(p, stack, inStack, canUse):
    if len(canUse) == 0:
        return
    s = sorted(canUse)
    canUseChange = False
    if s[0] != p[-1]:
        p.append(s[0])
        canUseChange = pushStack(s[0], stack, inStack, canUse)
        if canUseChange:
            extendP(p, stack, inStack, canUse)
    if not canUseChange:
        for i in range(1, len(s)):
            p.append(s[i])
            canUseChange = pushStack(s[i], stack, inStack, canUse)
            if canUseChange:
                extendP(p, stack, inStack, canUse)
            else:
                p.append(s[0])

k, m = [int(x) for x in input().split()]
p = []
stack = []
inStack = set()
canUse = set([x for x in range(1, k + 1)])
for i in range(m):
    x = int(input())
    p.append(x)
    pushStack(x, stack, inStack, canUse)

if len(canUse) == 0:
    printOut(p)
elif len(canUse) == k:
    p += sorted(canUse - inStack)
    for i in range(len(p) - 2, -1, -1):
        p.append(p[i])
    printOut(p)
else:
    extendP(p, stack, inStack, canUse)
    printOut(p)
