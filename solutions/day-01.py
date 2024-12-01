"""Solution for Advent of Code - Day 1"""

def solve_part_1(input_data):
    lst_left=[]
    lst_right=[]
    for i in input_data.split("\n"):
        split=i.split("   ")
        lst_left.append(int(split[0]))
        lst_right.append(int(split[1]))
            
    lst_left.sort()
    lst_right.sort()

    sum=0
    for i in range(len(lst_left)-1):
        sum+=abs(lst_right[i]-lst_left[i])
    
    return sum

def solve_part_2(input_data):
    lst_left=[]
    lst_right=[]
    for i in input_data.split("\n"):
        split=i.split("   ")
        lst_left.append(int(split[0]))
        lst_right.append(int(split[1]))
   
    sum=0
    for i in range(len(lst_left)-1):
        num=lst_left[i]
        cnt=lst_right.count(num)
        sum+=num*cnt

    return sum
