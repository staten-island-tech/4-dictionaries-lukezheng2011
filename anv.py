items = [

    {"name":"William without his organs","value":"0.01","itemtype":"human","rating":"4/10",},

    {"name":"(Overpriced) Pizza SLice","value":"7.99","itemtype":"food","rating":"7/10",},
    
    {"name":"Mr. Whalen's clock","value":"24.99","itemtype":"household","rating":"9/10",},

    {"name":"iPhone 17 - 256 GB","value":"799.99","itemtype":"eletronics","rating":"8/10",},

    {"name":"Staten Island Technical High School PE T-Shirt","value":"24.99","itemtype":"clothing","rating":"4/10",},

    {"name":"iPhone 17 - 512 GB","value":"999.99","itemtype":"eletronics","rating":"8/10",},

    {"name":"William's Shoes","value":"30.67","itemtype":"clothing","rating":"6/10",}

]

cost = 0
buy = 1
bought = []

while buy == 1:
    for index, item in enumerate(items):
        print(index, ":", item["name"])
    ab = int(input("Which item would you like. Enter the number: "))
    cost += (float(items[ab]["value"]))

    exact = round(cost,2)

    print(exact)







#print(items[0]["value"])
