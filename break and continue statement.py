# # 1. print string within str
# for val in "String":
#     if val == "i":
#         break
#     print(val)
# print("The end")
# # 2. print 1 to 4
# i = 0
# while i < 6:
#     x = i + 1
#     print(x)
#     i = x
#     if i == 4:
#         break
# print("the end")
# # 3. print string without i
# for val in "string":
#     if val == "i":
#         continue
#     print(val)
# print("the end")
# # 4. print 1 to 6 without 3
# i = 0
# while i < 6:
#     i = i + 1
#     if i == 3:
#         continue
#     print(i)
# print("the end")
# # 5. break in while loop
# num_sum = 0
# count = 0
# while count < 10:
#     num_sum = num_sum + count
#     count = count + 1
#     if count == 5:
#         break
# print("Sum of first ", count, "integers is: ", num_sum)
# # 6. break in for loop
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Declaring the tuple
# num_sum = 0
# count = 0
# for x in numbers:
#     num_sum = num_sum + x
#     count = count + 1
#     if count == 5:
#         break
# print("Sum of first ", count, "integers is: ", num_sum)
# # 7.
# for i in range(9):
#     if i > 3:
#         break
#     print(i)
# print("the end")
# # 8.
# i = 1
# while i < 9:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# print("the end")
# #9
# for x in range(4):
#    if (x==2):
#       continue
#    print(x)
# i = 0
# while (True):
#     if i < 10:
#         i = i + 1
#         continue
#     print(i+1, end="  ")
#     if i == 44:
#         break #stop the loop
#     i = i+1
#break kore eikhane chole asbe
while True:
    take_input = int(input("Give the number: \n"))
    if take_input <100:
        print("Try Again \n")
        continue
    if take_input >=100:
        print("Congratulations you give the number which is greater than 100")
        break