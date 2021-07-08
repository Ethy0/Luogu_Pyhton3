def out(target) :
    if target=="A" :
        print(num[0],end=" ")
    if target=="B" :
        print(num[1],end=" ")
    if target=="C" :
        print(num[2],end=" ")
    return
num = [0,0,0]
order = []
num[0],num[1],num[2]=map(int,input().split())
orders=input()
for x in orders :
    order.append(x)
num.sort()
for i in range(0,3) :
    out(order[i])