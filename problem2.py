#assuming a,b,c 

a = int(input("Starting number of organisims: "))

b = int(input("Average daily percentage increase:"))

c = int(input("Enter the number of days to display the final data:"))

print("Day Approximate              Population")
print("---------------------------------------")
for i in range (c):
  a=a+(b*a/100)
  print("",i+1,"                 ",a)

