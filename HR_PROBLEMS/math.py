import math
AB=int(input())
BC=int(input())
AC=math.sqrt(AB**2+BC**2)
MC=AC/2
BM=math.sqrt(BC**2-MC**2)
angle=0
if (-1<=(MC/BC)<=1):
    angle=math.degrees(math.asin(MC/BC))
elif (-1<=(BM/BC)<=1):
    angle=math.degrees(math.acos(BM/BC))
sym=u"\N{DEGREE SIGN}"
print(str(math.floor(angle+0.5))+sym)

