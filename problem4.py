a=[]

num=int(input("myNumbers:"))

for i in range (1,num+1):

  a.append(i)
print(a)

greater=int(input("Enter the grater point:"))

b=[]
for i in range (1,num+1):

  if(a[i-1]>greater):
    b.append(a[i-1])
else: 
 pass

print(b)