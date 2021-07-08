import math
num = []
value = []
money = []
x=int(input())
for i in range(0,3) :
    a,b=map(int,input().split())
    num.append(a)
    value.append(b)
for i in range(0,3) :
    money.append(value[i]*int(math.ceil(x/num[i])))
money.sort(reverse=True)
print(money.pop())