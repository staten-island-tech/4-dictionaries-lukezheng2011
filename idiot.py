def gamble(a,b,c,d):
    remainder=0
    each = 0
    total = 0
    amount = 0

    while a>=0:
        for i in range(2):
            if a % 3 == i:
                
                remainder = i
                each = (a - remainder)/3
                b = b+each
                c = c+each
                d = d+each
                
                
                a = a - (3 * each)
                amount += a + (3*each)
                total = total + amount

                
            if remainder == 1:
                b = b + 1
                a = a-1
                remainder = 0
            elif remainder == 2:
                b = b + 1
                c = c +1
                a = a - 2
                remainder = 0
        
        a -= 1
        amount += 1
        
        if b - 35 > 0:
            a = a +30
            a -= 1
            amount += 1
           # total = total + 30
        if c - 100 > 0:
            a = a + 60
            a -= 1
            amount += 1
            #total = total + 60
        if d - 10 > 0:
            a = a + 9
            a -= 1
            amount += 1
           # total = total + 9
            
        break

    print(f"Martha can play {amount} times before going broke")

gamble(77,4,9,3)
#gamble(int(input("How many quarters do you have: ")),int(input("How many times has machine one been used?")),int(input("How many times has machine two been used?")),int(input("How many times has machine three been used?")))