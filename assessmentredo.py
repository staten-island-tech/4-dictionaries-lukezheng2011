def gamble(a,b,c,d):

    total = 0

    while a > 0:
        
        b = b+1
        total = total + 1
        a = a-1
        
        if b - 30 >= 0:
            a = a + 30
            b = b-30

        if a == 0:
            break



        c = c+1
        total = total + 1
        a = a-1
        
        if c - 100 >= 0:
            a = a + 60
            c = c-100
        
        if a == 0:
            break



        d = d+1
        total = total + 1
        a = a-1
        
        if d - 10 >= 0:
            a = a + 9
            d=d-10

        if a == 0:
            break





    print(f"Martha can play {total} times.")
gamble(48,3,10,4)