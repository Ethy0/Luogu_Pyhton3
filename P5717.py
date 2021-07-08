def tri(x,y,z) :
    if ((x+y)>z) and ((x+z)>y) and ((y+z)>x) and (abs(x-y)<z) and (abs(x-z)<y) and (abs(y-z)<x) :
        return True
    else :
        return False
def right(x,y,z) :
    if x**2+y**2==z**2 :
        return True
    else :
        return False
def acute(x,y,z) :
    if x**2+y**2>z**2 :
        return True
    else :
        return False
def obtuse(x,y,z) :
    if x**2+y**2<z**2 :
        return True
    else :
        return False
def iso(x,y,z) :
    if x==y or x==z or y==z :
        return True
    else :
        return False
def equal(x,y,z) :
    if x==y and x==z :
        return True
    else :
        return False
a,b,c=map(int,input().split())
num = [a,b,c]
num.sort()
if tri(num[0],num[1],num[2])==False :
    print("Not triangle")
    exit()
if right(num[0],num[1],num[2]) :
    print("Right triangle")
if acute(num[0],num[1],num[2]) :
    print("Acute triangle")
if obtuse(num[0],num[1],num[2]) :
    print("Obtuse triangle")
if iso(num[0],num[1],num[2]) :
    print("Isosceles triangle")
if equal(num[0],num[1],num[2]) :
    print("Equilateral triangle")