flag=0
y,m=map(int,input().split())
if (y%4==0 and y%100!=0) or (y%100==0 and y%400==0) :
    flag=1
if m==1 or m==3 or m== 5 or m==7 or m==8 or m==10 or m==12 :
    print("31")
if m==4 or m==6 or m==9 or m==11 :
    print("30")
if m==2 and flag==1 :
    print("29")
if m==2 and flag==0 :
    print("28")