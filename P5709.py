m,t,s=map(int,input().split())
if t == 0 :
    print("0")
    exit()
if s == 0 :
    print(m)
    exit()
left=int(m-(s/t))
if left<=0:
    print("0")
    exit()
print(left)