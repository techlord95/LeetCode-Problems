# Python Operators with Examples and Outputs


# ==========================================
# 1. Arithmetic Operators
# ==========================================

a = 10
b = 3

print(a + b)   # Addition Operator (+) → 13
print(a - b)   # Subtraction Operator (-) → 7
print(a * b)   # Multiplication Operator (*) → 30
print(a / b)   # Division Operator (/) → 3.3333333333333335
print(a // b)  # Floor Division Operator (//) → 3 (quotient)
print(a % b)   # Modulus Operator (%) → 1 (remainder)
print(a ** b)  # Exponentiation Operator (**) → 1000


# ==========================================
# 2. Assignment Operators
# ==========================================

x = 5
print(x)       # Assignment Operator (=) → 5

x += 3
print(x)       # Add and Assign Operator (+=) → 8

x -= 2
print(x)       # Subtract and Assign Operator (-=) → 6

x *= 4
print(x)       # Multiply and Assign Operator (*=) → 24

x /= 6
print(x)       # Divide and Assign Operator (/=) → 4.0

x //= 2
print(x)       # Floor Divide and Assign Operator (//=) → 2.0

x %= 2
print(x)       # Modulus and Assign Operator (%=) → 0.0

x = 2
x **= 3
print(x)       # Exponent and Assign Operator (**=) → 8


# ==========================================
# 3. Comparison Operators
# ==========================================

p = 10
q = 20

print(p == q)  # False
print(p != q)  # True
print(p > q)   # False
print(p < q)   # True
print(p >= q)  # False
print(p <= q)  # True


# ==========================================
# 4. Logical Operators
# ==========================================

x = True
y = False

print(x and y) # False
print(x or y)  # True
print(not x)   # False


# ==========================================
# 5. Bitwise Operators
# ==========================================

m = 5   # Binary: 0101
n = 3   # Binary: 0011

print(m & n)   # 1
print(m | n)   # 7
print(m ^ n)   # 6
print(~m)      # -6
print(m << 1)  # 10
print(m >> 1)  # 2


# ==========================================
# 6. Identity Operators
# ==========================================

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)      # True
print(list1 is list3)      # False
print(list1 is not list3)  # True


# ==========================================
# 7. Membership Operators
# ==========================================

nums = [1, 2, 3, 4, 5]

print(3 in nums)       # True
print(10 in nums)      # False
print(6 not in nums)   # True


# ==========================================
# 8. Conditional (Ternary) Operator
# ==========================================

age = 18
result = "Adult" if age >= 18 else "Minor"
print(result)          # Adult


# ==========================================
# 9. Operator Precedence Example
# ==========================================

result = 10 + 2 * 3
print(result)          # 16

result = (10 + 2) * 3
print(result)          # 36


# ==========================================
# 10. Special Operators with Strings
# ==========================================

str1 = "Hello"
str2 = "World"

print(str1 + " " + str2)  # Hello World
print(str1 * 3)            # HelloHelloHello


# ==========================================
# 11. Special Operators with Lists
# ==========================================

list_a = [1, 2]
list_b = [3, 4]

print(list_a + list_b)  # [1, 2, 3, 4]
print(list_a * 2)       # [1, 2, 1, 2]


# ==========================================
# 12. Walrus Operator (:=)
# ==========================================

print(num := 15)   # 15
print(num + 5)     # 20


# ==========================================
# 13. Matrix Multiplication Operator (@)
# ==========================================

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A @ B)
# [[19 22]
#  [43 50]]


