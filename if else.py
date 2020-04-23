# list1 = ["a", "b", "c"]
# print("f" not in list1)
# if "f" not in list1:
#  print("no it isn't in list")
a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))
x = input("Which operation do you want\n"
          "+ for addition\n"
          "- for subtraction\n"
          "* for multiplication\n"
          "/ for divination\n")
set1 = [45, 3]
set2 = [56, 6]
set3 = [56, 9]
if x == '*':
    if a in set1 and b in set1:
        print(555)
if x == '/':
    if a in set2 and b in set2:
        print(4)
elif x == '+':
    if a in set3 and b in set3:
        print(77)
elif x == '+':
    print(a + b)
elif x == '-':
    print(a - b)
elif x == '*':
    print(a * b)
else:
    print(a / b)
