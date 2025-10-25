def gamble(a, b, c, d):
    plays = 0
    
    while a > 0:
        # Machine 1
        plays += 1
        a -= 1
        b += 1
        if b == 35:
            a += 30
            b = 0
        if a == 0:
            break
        
        # Machine 2
        plays += 1
        a -= 1
        c += 1
        if c == 100:
            a += 60
            c = 0
        if a == 0:
            break
        
        # Machine 3
        plays += 1
        a -= 1
        d += 1
        if d == 10:
            a += 9
            d = 0
        if a == 0:
            break
    
    print(f"Martha can play {plays} times before going broke.")
gamble(int(input("How many quarters does Martha have: ")),int(input("How much has machine one been used: ")),int(input("How much has machine two been used: ")),int(input("How much has machine three been used: ")))