def are_coprime(a, b):
    while b:
        a, b = b, a % b
    return a == 1
print("Gokul Biju : SJC22MCA-2028 : S3MCA")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if are_coprime(num1, num2):
    print("Numbers are coprime.")
else:
    print("Numbers are not coprime.")
