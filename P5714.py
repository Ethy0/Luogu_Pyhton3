m,h=map(float,input().split())
x=m/(pow(h,2))
if x<18.5 :
    print("Underweight")
if x>=18.5 and x<24 :
    print("Normal")
if x>=24 :
    print('%.6g' % x)
    print("Overweight")