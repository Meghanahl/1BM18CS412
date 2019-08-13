a=[]
b=[]
size=int(input("enter the size"))
print("enter the element")
for i in range(0,size):
    element=int(input())
    a.append(element)
    if(a[i]%2==0):
       b.append(a[i])
print("input list",a)
print("even list",b)
