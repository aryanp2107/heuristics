def main():
    # Building a greedy algorithm to find the minimum number of coins
    # get the amount of change to be made
    while True:
        change = float(input("Change owed: "))
        if change > 0:
            break
    # Convert the change amount to cents
    cents = round(change * 100)
    # Initialize the number of coins to 0
    coins = 0
    # greedy algorithm to find the minimum number of coins
    while cents >= 25:
        cents -= 25
        coins += 1
    while cents >= 10:
        cents -= 10
        coins += 1
    while cents >= 5:
        cents -= 5
        coins += 1
    while cents >= 1:
        cents -= 1
        coins += 1
    # Print the number of coins
    print(coins)

if __name__ == "__main__":
    main()
