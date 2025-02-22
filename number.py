num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
    print(f"{num} is Prime")
else:
    print(f"{num} is Not Prime")
