"""Solution for Advent of Code - Day 3"""
import re
def solve_part_1(input_data):
    """
    Solve Part 1 of the challenge for this day.
    """
    regexPattern=r"mul\((\d{1,3}),(\d{1,3})\)"
    matches=re.findall(regexPattern,input_data)
    print(matches,sep='\n')
    tsum=0
    for num1,num2 in matches:
        tsum+=int(num1)*int(num2)
    
    return tsum

def solve_part_2(input_data):
    """
    Solve Part 2 of the challenge for this day.
    """
    # TODO: Implement Part 2 solution
    return None

# Optional: Add helper functions if needed
