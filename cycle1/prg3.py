print("Gokul Biju : SJC22MCA-2028 : S3MCA")
a=(int(input("enter the first side : ")))
b=(int(input("enter the second side : ")))
c=(int(input("enter the third side : ")))
if  a==b==c  :
    print("equailateral triangle")
elif a==b or a==c or b==c:
    print("isosceles triangle")
else:
    print("scalane triangle")