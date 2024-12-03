"""Solution for Advent of Code - Day 2"""

def solve_part_1(input_data):
    lsts=[]
    for i in input_data.split("\n"):
        lst2=[]
        for j in i.split(" "):
            lst2.append(int(j))
        lsts.append(lst2)
    
    safeCount=0
    for lst in lsts:
        diffs=[]
        for i in range(len(lst) - 1):
            diffs.append(lst[i + 1] - lst[i])

        inc=True
        dec=True
        for diff in diffs:
            if diff<=0:
                inc =False
            if diff>=0:
                dec=False
        
        safe=True
        for diff in diffs:
            if not (1 <= abs(diff) <= 3): 
                safe=False
                break
        
        if (inc or dec) and safe:
            safeCount+=1        

    return safeCount

def solve_part_2(input_data):
    lsts=[]
    for i in input_data.split("\n"):
        lst2=[]
        for j in i.split(" "):
            lst2.append(int(j))
        lsts.append(lst2)
    
    safeCount=0
    for lst in lsts:
        diffs=[]
        for i in range(len(lst) - 1):
            diffs.append(lst[i + 1] - lst[i])

        inc=True
        dec=True
        checkInc=1
        checkDec=1
        for diff in diffs:
            if diff<=0:
                if checkInc>0:
                    checkInc-=1
                else:
                    inc =False
            if diff>=0:
                if checkDec > 0:
                    checkDec -= 1
                else:
                    dec = False
        
        safe=True
        for diff in diffs:
            if not (1 <= abs(diff) <= 3): 
                safe=False
                break
                
        if (inc or dec) and safe:
            safeCount+=1        

    return safeCount