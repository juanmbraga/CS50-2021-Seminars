# Write a program that asks the user to type in a number n and then prints a pyramid of hash marks of height n. (alligned to the right side)

while True:
    height = int(input("height of the pyramid: "))
    if height > 0:
        break

for i in range(height):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")
    print()
    
# Alternative by Justin Tse in edstem.org (I would never imagine this was possible in Python!)
##for i in range(n):
##    print(" " * (n - i - 1) +  "#" * (i + 1) + "  " + "#" * (i + 1))
