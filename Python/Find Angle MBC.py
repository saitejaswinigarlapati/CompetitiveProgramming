"""
Point  'M' is the midpoint of hypotenuse .
You are given the lengths 'AB' and 'BC' .
Your task is to find  angle MBC in degrees.

"""
import math

AB=int(input("Length of side AB : "))
BC=int(input("Length of side BC : "))

angle_r=math.atan(AB/BC)
angle=round(math.degrees(angle_r))
print (str(angle) + chr(176))
