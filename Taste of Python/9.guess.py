import random

print("Guess the number! You have three attempts.")
number = random.randint(1,10)
for i in range(3):
    while True:
        attempt = int(input("number between 1 and 10: "))
        # || didn't work, thankfully python seems intuitive!
        ## I also had used the wrong variable, and the wrong comparison (OR and not AND)
        if attempt > 0 and attempt < 11: 
            break
    if attempt > number:
        print("Hmm that's too high.")
    elif attempt < number:
        print("Hmm that's too low.")
    else:
        print("Congrats! You are correct!")
        break
    
# How to not print this if user guessed correctly? (without using another variable if possible)
## The "else" statement can be used in conjunction with "for" loops, and it's code will be executed if no "break" statements were called during the loop
else: 
    print("You have failed. The number was", number)
    
# Thanks to Johannes Slotta on edstem.org for the tip!