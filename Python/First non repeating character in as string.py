# Write a python code to find the first non -repeating character in a string

def find(s):
    char={}
    for i in s:
        char[i]=char.get(i,0)+1
    for i in s:
        if char[i]==1:
            return i
    return None

s="nxtware"
print(f"First non repeating char in {s} : {find(s)}")

def finds(s):
    for i in s:
        if s.count(i)==1:
            return i
    return None
print(f"First non repeating char in {s} : {finds(s)}")
