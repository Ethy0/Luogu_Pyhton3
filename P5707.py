import math
s,v=map(float,input().split())
t=math.ceil(s/v) + 10
h=7-int(t/60)
if h < 0:
    h+=24
m=60-t%60
print(int(str(h).zfill(2)),end=":")
print(int(str(m).zfill(2)))
