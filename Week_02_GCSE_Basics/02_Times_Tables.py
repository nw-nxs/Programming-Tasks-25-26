"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
def multiplication(nums):
    num = int(input("Enter a number"))
    for i in range(len(nums)):
        mult = nums[i]*num
        print(mult)
multiplication(nums)
