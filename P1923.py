n,k=map(int,input().split())
num=list(map(int,input().split()))
num.sort(reverse=True)
k+=1
print(num.pop(-k))