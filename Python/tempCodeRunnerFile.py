# def countResiduePrefixes(s):
#     n=len(s)
#     residueCount=0
#     for i in range(1,n):
#         a=s[:i]
#         c=len(set(a))
#         if c== i%3:
#             residueCount+=1
#     return residueCount

## Complexity: O(n^2) because of prefix s[:i] can be optimized by maintaining a running set

## Optimized version:

def countResiduePrefixes(s):
    residualCount=0
    seen=set()
    for i,ch in enumerate(s,1):
        seen.add(ch)
        if len(seen) == i%3:
            residualCount+=1
    return residualCount

## Complexity O(n)
        

s="bob"
print(countResiduePrefixes(s))
