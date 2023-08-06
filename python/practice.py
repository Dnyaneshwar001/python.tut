l1=[ 1,2,'hello',3.4]
print(l1 [0:])
print(l1[:])
print(l1[2:4])
print(l1[:4])
print(l1[1:4:2])
print(l1[-1])
print(l1[-3:-1])
l1[2]=10
print(l1)
l1[3:4]=[89,36]
print(l1)
#repetation
l2=l1*2
print(l2)
#concatenate
l3=l1+l2
print(l3)
print(len(l3))
for l1 in  l3:
    print(l1)
#taking user inpute in the list
l4=[]
n=int(input( "Enter number of elements:"))
for i in range(0,n):
    ele=int(input("enter the element"))
    l4.append(ele)
    print(l4)
# remove,length,minmum value,maximum value
l5=[5,6,9,5,78,2,65]
l5.remove(78)
print(l5)
print(len(l5))
print(min(l5))
print(max(l5))

#tuple
t1=(1,5,6,6,4,64,5,6,4,5,4,)
print(t1)
print(t1[0])
t1=t1*3
print(t1)