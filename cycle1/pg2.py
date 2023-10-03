print("Gokul Biju : SJC22MCA-2028 : S3MCA")
n=int(input("enter the number : "))
n1=0
n2=1
print("fibonacci series:\n",n1,n2,end=" ")
for i in range(2,n):
  n3=n1+n2
  n1=n2
  n2=n3
  print(n3,end=" ")
