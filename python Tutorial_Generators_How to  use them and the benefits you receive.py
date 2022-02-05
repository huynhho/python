##def square_numbers(nums):
##    result = []
##    for i in nums:
##        result.append(i*i)
##        print(result)
##    return result
##my_nums = square_numbers([1,2,3,4,5])
##print(my_nums)

def square_numbers(nums):
    for i in nums:
        yield(i*i)
my_nums = square_numbers([1,2,3,4,5])
##print (next(my_nums))
print(square_numbers([1,10,100]))
