try:
    actual_cost = int(input("enter cost: "))
    sale_cost = int(input("enter sale: "))
    if sale_cost > actual_cost:
        amount = sale_cost - actual_cost
        print("profit is: {0}".format(amount))
    else:
        print("no profit")
except ValueError:
    print("no profit")