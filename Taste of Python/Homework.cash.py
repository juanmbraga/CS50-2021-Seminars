print("Find the minimum amount of coins to make change for a given amount of money.")
money = float(input("How much: "))
total = 0

total += int(money / 0.25)
money = money % 0.25
total += int(money / 0.10)
money = money % 0.10
total += int(money / 0.05)
money = money % 0.05
total += int(money / 0.01)
money = money % 0.01

print("The minimum amount of coins necessary is", total)