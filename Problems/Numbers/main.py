# put your python code here
def multiply(num1, *nums):
    result = num1
    for num in nums:
        result *= num
    return result
#
# print(multiply(112))
# print(multiply(112,234, 3453, 1231))