def main():
    score1 = int(input("Score 1: "))
    score2 = int(input("Score 2: "))
    score3 = int(input("Score 3: "))
    
    printScore(score1)
    printScore(score2)
    printScore(score3)
    
def printScore(n):
    for i in range(n):
        print("#", end="")
    print()
    
main()