# When you use the def keyword, you are creating a function and binding it to a specific
# name in memory. A lambda allows you to create a function on the fly without giving it a 
# name (hence "anonymous").


# Syntax

# lambda aurgument : expression

# def sqaure(x):
#     return x**2 
    
# square_lambda = lambda x:x**2 # should not be used like this in practice 
# print(square_lambda(5))


# Lambdas shine when you need a throwaway function for a short period,
# usually to pass as an argument to another function (known as a Higher-Order Function).

# Example 1 

# students = [("Alice", 88), ("Bob", 95), ("Charlie", 72)]

# # The 'key' argument expects a function. 
# # The lambda says: "For every item x, look at x[1] for sorting."
# sorted_students = sorted(students, key=lambda x: x[1])

# print(sorted_students) 
# # Output: [('Charlie', 72), ('Alice', 88), ('Bob', 95)]


# # map() applies a function to every item in an iterable.


# numbers = [1, 2, 3, 4]
# # Square every number in the list
# squared = list(map(lambda x: x**2, numbers))
# print(squared) # Output: [1, 4, 9, 16]


# # C. Filtering Data (filter)
# filter() keeps items where the function evaluates to True.


# numbers = [1, 2, 3, 4, 5, 6]
# # Keep only the even numbers
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens) # Output: [2, 4, 6]


# This is an advanced trap that catches many developers. Look at this code:


# # We want to create 3 functions that add 0, 1, and 2 respectively.
# adders = [lambda x: x + i for i in range(3)]

# # We expect adders[0](10) to return 10 (10 + 0).
# print(adders[0](10)) # Output: 12 !!!
# print(adders[1](10)) # Output: 12 !!!

# Why did that happen? Python lambdas use late binding. They don't look at the value of i when the lambda is created; they look at the value of i when the lambda is called. By the time we call them, the loop has finished and i is sitting at 2.

## The Fix: You force early binding by passing i as a default argument.


# adders = [lambda x, i=i: x + i for i in range(3)]
# print(adders[0](10)) # Output: 10 (Working perfectly!)