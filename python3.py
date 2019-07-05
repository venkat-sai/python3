x=list(input())
k=0
while(k<len(x)):
    temp=x[k]
    x[k]=x[k+1]
    x[k+1]=temp
    k+=2
print("".join(x))
