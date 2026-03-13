def gamble(quarters,slot1,slot2,slot3):
    plays= 0
    one=35-slot1
    two=100-slot2
    three=10-slot3
    stage = 1
    while quarters != 0:
        quarters -= 1
        plays + 1
        if stage == 1:
            one += 1
            stage == 2
            if one == 35:
                quarters += 59
                one == 0
                
        if stage == 2:    
            two + 1
            stage ==3
            if two == 100:
                quarters += 59
            two == 0
            
        if stage == 3:
            three + 1
            stage == 1
            if three == 10:
                quarters += 8
            three == 0 
            
        if quarters == 0:
            print(plays)
gamble(48,3,10,4)
    
