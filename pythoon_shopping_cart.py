# make variable for in input
# make an empty dictionary
# make a def that allows user to add/delete items
# make def be able to show cart at any time
# make def go until user presses quit
# after def quits print all items, prices, quantites, and total

def shopping_cart():
    cart = {}
    show = 0
    while True:
        user_in = input("What do you want to do? Add/Remove/Clear/Show/Quit: \n").lower()
        if user_in == "add":
            item = input("What Item would you like to add?:  \n")
            if item in cart:
                print("This item is already in the cart! \n")
                choice1 = input("Would you like to add more? y/n:  \n").lower()
                if choice1 == "y":
                    quantity = int(input("How much would you like to add?:  \n"))
                    quantity += quantity
                    cart[item] = [quantity, price]
                    show = 1
                elif choice1 == "n":
                    pass
            else:
                price = float(input("How much does the item cost?:  \n"))
                quantity = int(input("How many of the item would you like?:  \n"))
                cart[item] = [quantity, price]
                show = 1
        elif user_in == "remove":
            print("These are all the items in your cart currently \n")
            for item in cart:
                print(f"{cart[item][0]} {item}(s) -----> ${cart[item][1]}")
            item_r = input("Which item would you like to remove?:  \n")
            if item_r in cart:
                choice2 = input("Are you sure you want to remove this item? y/n:  \n").lower()
                if choice2 == "y":
                    removed = int(input("How many would you like to remove?:  \n"))
                    quantity -= removed
                    cart[item] = [quantity, price]
                elif choice2 == "n":
                    pass
            else:
                print("That item is not in your cart!\n")
        elif user_in == "clear":
            choice = input("Are you sure that you want to clear your cart? \nThis choice is not reversible y/n:  \n").lower()
            if choice == "y":
                cart.clear()
                print("Your cart has been cleared\n")
                show = 0
            elif choice == "n":
                pass
            else:
                print("Invalid choice\n")
        elif user_in == "show":
            total_cost = []
            if show == 1:
                for item in cart:
                    item_price = cart[item][0] * cart[item][1]
                    print(f"{item} : {cart[item][0]} X ${cart[item][1]} = ${item_price}")
                    total_cost.append(item_price)
                total = sum(total_cost)
                print(f"Your total is {total}\n")
            elif show == 0:
                print("Your cart is empty!\n")
        elif user_in == "quit":
            print(" ")
            break
        else:
            print("Invalid choice\n")
    if show == 1:
        print("Here is your receipt: \n")
        for item in cart:
            print(f"{cart[item][0]} {item}(s) -----> ${cart[item][1]}")
        print(f"Your total is: {total}\n")
    elif show == 0:
        pass
    print("Hope to see you again soon!")



shopping_cart()