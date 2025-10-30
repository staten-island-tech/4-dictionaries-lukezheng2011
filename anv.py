items = [

    {"name":"William without his organs","value":"0.01","itemtype":"human","rating":"4/10",},

    {"name":"(Overpriced) Pizza SLice","value":"7.99","itemtype":"food","rating":"7/10",},
    
    {"name":"Mr. Whalen's clock","value":"24.99","itemtype":"household","rating":"9/10",},

    {"name":"iPhone 17 - 256 GB","value":"799.99","itemtype":"eletronics","rating":"8/10",},

    {"name":"Staten Island Technical High School PE T-Shirt","value":"24.99","itemtype":"clothing","rating":"4/10",},

    {"name":"iPhone 17 - 512 GB","value":"999.99","itemtype":"eletronics","rating":"8/10",},

    {"name":"William's Shoes","value":"30.67","itemtype":"clothing","rating":"1/10",},

    {"name":"SITHS Bake Sale Pizza Slice","value":"2.00","itemtype":"food","rating":"10.67/10",},

    {"name":"ShopRite Donut","value":"1.00","itemtype":"food","rating":"8/10",},

    {"name":"Stupidly Loud Alarm Clock","value":"10.99","itemtype":"household","rating":"10.67/10",},

    {"name":"Mr. Whalen's Sanity","value":"14000.00","itemtype":"food","rating":"10.67/10",}




]

cost = 0
buy = 1
bought = []

while buy == 1:
    for index, item in enumerate(items):
        print(index, ":", item["name"])
    ab = int(input("Which item would you like. Enter the number: "))
    cost += (float(items[ab]["value"]))
    bought.append(items[ab]["name"])

    exact = round(cost,3)

    print(exact)
    print(bought)

    buy = int(input("Enter 1 to continue purchasing, enter 2 to check out: "))


print(f"Your total cost is {exact} and you've pucrhased the following items: {bought}.")








#print(items[0]["value"])
