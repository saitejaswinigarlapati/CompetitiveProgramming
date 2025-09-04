'''
You are given three integers x, y, and z, representing the positions of three people on a number line:

x is the position of Person 1.
y is the position of Person 2.
z is the position of Person 3, who does not move.
Both Person 1 and Person 2 move toward Person 3 at the same speed.

Determine which person reaches Person 3 first:

Return 1 if Person 1 arrives first.
Return 2 if Person 2 arrives first.
Return 0 if both arrive at the same time.
Return the result accordingly.

'''

def findClosest(x: int, y: int, z: int) -> int:
    p1=abs(z-x)
    p2=abs(z-y)
    if p1 <p2:
        return 1
    elif p1>p2:
        return 2
    else:
        return 0
    
x = 2
y = 5
z = 6

print(findClosest(x,y,z))

# Input: x = 2, y = 5, z = 6
# Output: 2

# Input: x = 2, y = 7, z = 4
# Output: 1

# Input: x = 1, y = 5, z = 3
# Output: 0