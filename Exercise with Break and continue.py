i = 0
while i < 100:
    take_input = int(input("Enter the number:\n"))
    if take_input >= 100:
        print("You have given the number which is greater than 100\n")
        break
    print("Try again!\n")
#another_way
# while(True):
#     inp = int(input(("Enter a number:\n")))
#     if inp > 100:
#         print("You have given the number which is greater than 100\n")
#         break
#     else:
#         print("Try again!\n")
#         continue


