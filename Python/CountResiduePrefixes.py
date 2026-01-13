'''
You are given a string s consisting only of lowercase English letters.

A prefix of s is called a residue if the number of distinct characters in the prefix is equal to len(prefix) % 3.

Return the count of residue prefixes in s.

A prefix of a string is a non-empty substring that starts from the beginning of the string and extends
to any point within it.

Test Cases:

Input: s="abc"
Output: s

Input: s="bob"
Output:2

Input: s= "dd"
Output: 1

'''


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


