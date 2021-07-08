from fractions import Fraction
a,b,c=map(int,input().split())
num = [a,b,c]
num.sort()
print(str(Fraction(num[0],num[2]).numerator)+"/"+str(Fraction(num[0],num[2]).denominator))