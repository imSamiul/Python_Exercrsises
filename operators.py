# operators In Python
# Arithmetic Operator
# Assignment Operator
# Comparison Operator
# Logical Operator
# Identify Operator
# Membership Operator
# Bitwise operator

# 1.Arithmetic Operator
print("5+6 is ", 5 + 6)
print("5-6 is ", 5 - 6)
print("5*6 is ", 5 * 6)
print("5/6 is ", 5 / 6)
print("5//6 is ", 5 // 6)
# this only take integer value
print("15//6 is ", 15 // 6)
# this only print integer value, ignore what comes after decimal point
print("5**6 is ", 5 ** 6)
# this will print as an exponent or power like 5 to the power 6
print("5**3 is ", 5 ** 3)
# this will print as an exponent or power
print("5%3 is ", 5 % 3, "\n")
# this will print as a reminder.

# 2. Assignment operator(to store value in a variable)
x = 5
print(x)
x += 7
print(x)
x %= 7
print(x, "\n")

# 3. Comparision Operator
i = 8
print(i == 5)
i = 5
print(i == 5)
print(i != 5)
print(i > 5)
print(i < 5)
print(i >= 5)
print(i <= 5, "\n")

# 4. Logical Operator
a = True
b = False
print(a and b)
print(a or b, "\n")

# 5. Identify Operator
a = True
b = False
print(a is b)
print(a is not b)
print(5 is not 7, "\n")

# 6. Membership Operators
list = [2, 4, 5, 6, 7, 6, 7]
print(4 in list)
print(324 not in list)
print(67 in list, "\n")

# 6. Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
print(0 & 1)
# 0 and 0 =0
# 0 and 1 =0
# 00 = 0
print(0 | 1)
# 0 or 0 = 0
# 0 or 1 = 1
# 01 = 1
print(0 | 3)
# 0 or 1 = 1
# 0 or 1 = 1
# 11 = 3
