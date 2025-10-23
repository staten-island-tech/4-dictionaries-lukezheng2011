def gamble(a,b,c,d):
    remainder=0
    machone=b
    machtwo=c
    machthree=d
    each = 0
    total = a

    while a>=0:
        for i in range(2):
            if a % 3 == i:
                remainder = i
                each = (a - remainder)/3
                machone = machone+each
                machtwo = machtwo+each
                machthree = machthree+each
                a = 0
            
        if remainder == 1:
            machone = machone + 1
            remainder = 0
        elif remainder == 2:
            machone = machone + 1
            machtwo = machtwo +1
            remainder = 0
        
        if machone - 35 > 0:
            a = a +30
            total = total + 30
        if machtwo - 100 > 0:
            a = a + 60
            total = total + 60
        if machthree - 10 > 0:
            a = a + 9
            total = total + 9
        break

    print(f"Martha can play {total} times before going broke")

gamble(input)


