l= 0

num = int(input("Enter the number of years: "))
while(l<=num):

   j = 0
   k = 0
   total=0

   while(j<12):

      print("Enter the rainfall amount for the month:", j+1, "")
      k=int(input())
      total=total+k
      j+=1
      l=l+1

print("For 12 months total rainfall:", total,"inches")
print("Average monthly rainfall:", total/j)
      