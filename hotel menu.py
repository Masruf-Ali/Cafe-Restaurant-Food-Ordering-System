menu = {
    'Pizza':40,
    'Pasta':50,
    'Salad':60,
    'Burger':70,
    'Coffee':15,
    'Tea':10,

}
print("Welcome to our Caffe")
print(" Pizza: Rs40\n Pasta: Rs50\n Salad: Rs60\n Burger: Rs70\n Coffee: Rs15\n Tea: Rs10")

order_total = 0

item_1 = input("Enter the name of item which you want:-")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"{item_1} is  not avilable in our ceffa")
    print("Please order somthing which is avilable in our ceffa")
    print("nehi to gand mara or nikal m***r C***D")


another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes" or "yes":
    item_2 = input("Enter the name of item")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"{item_2} is  not avilable in our ceffa")
        print("Please Order Something else ")



another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes" or "yes":
    item_3 = input("Enter the name of item")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"Item {item_3} has been added to order")
    else:
        print(f"{item_3} is  not avilable in our ceffa")
        print("Please Order Something else ")



another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes" or "yes":
    item_4 = input("Enter the name of item")
    if item_4 in menu:
        order_total += menu[item_4]
        print(f"Item {item_4} has been added to order")
    else:
        print(f"{item_4} is  not avilable in our ceffa")
        



print(f"The total amount to pay of Orders items {order_total}")


    


