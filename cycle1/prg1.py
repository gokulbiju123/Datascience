print("Gokul Biju : SJC22MCA-2028 : S3MCA")
start=int(input("enter the first no of the intervel : "))
end=int(input("enter the last number of the intervel : "))
non_primes = []
for num in range(start,end+1):
    if num<2:
        non_primes.append(num)
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                non_primes.append(num)
                break
if non_primes:
    print("non_prime numbers in interval are:")
    print(non_primes)
else:
    print("there are no non prime numbers in the intervel [{start},{end}]")