
##* filter() - Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.

nums = [1, 5, 3, 2, 8, 90, 87, 56, 34]
is_even = lambda x : x % 2 == 0
even_nums = filter(is_even, nums)

print(even_nums)  # filter object
print(list(even_nums))  # [2, 8, 90, 56, 34]

##* ALTERNATIVE: list comprehension

even_nums = [i for i in nums if i % 2 == 0]
print(even_nums)  # [2, 8, 90, 56, 34]