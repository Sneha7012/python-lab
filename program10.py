n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

if n1 > n2 and n1 > n3:
    print(f"Largest number is: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"Largest number is: {n2}")
elif n3 > n1 and n3 > n2:
    print(f"Largest number is: {n3}")
else:
    print("There is a tie for the largest number.")
