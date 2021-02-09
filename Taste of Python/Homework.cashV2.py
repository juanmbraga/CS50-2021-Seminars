print("Find the minimum amount of coins to make change for a given amount of money.")

money = float(input("How much: "))

# According to https://blog.softhints.com/python-declare-multiple-variables/
total = quarters = dimes = nickels = pennies = 0

quarters = int(money / 0.25)
money = money % 0.25
dimes = int(money / 0.10)
money = money % 0.10
nickels = int(money / 0.05)
money = money % 0.05
pennies = int(money / 0.01)
money = money % 0.01

total = quarters + dimes + nickels + pennies

print("The minimum amount of coins necessary is", total)

print("The necessary coins are ", end="")
if quarters > 0:
    print(quarters, "quarter(s) ", end="")
if dimes > 0:
    print(dimes, "dime(s)" , end="")
if nickels > 0:
    print(nickels, "nickel(s) ", end="")
if pennies > 0:
    print(pennies, "pennies ", end="")