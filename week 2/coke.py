def main():
    """Dr.Pepper is actually amazing too!"""
    valid_coins = [25, 10, 5]
    cost = 50
    tendered = 0

    while tendered < cost:
        print(f"Amount Due: {cost - tendered}")
        try:
            money = int(input("Insert Coin: ").strip())
        except ValueError:
            print("Please insert a valid coin (5, 10, or 25).")
            continue

        if money in valid_coins:
            tendered += money
        else:
            print("Invalid coin. Please insert 5, 10, or 25 cents.")

    print(f"Change Owed: {tendered - cost}")


main()
