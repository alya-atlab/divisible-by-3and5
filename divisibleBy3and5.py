x = int(input("Enter x: "))
for n in range (1, x):
    if(n % 3 == 0 and n % 5 == 0):
        print(n)