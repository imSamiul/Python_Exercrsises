# f = open("harry2.txt", "a")
# f.write("Harry is a good person\n")
# f.close()


# f = open("harry2.txt", "w")
# a = f.write("Harry is a good person\n")
# print(a)
# f.close()

f = open("harry2.txt", "r+")
a = f.read()
print(a)
content = f.write("Thank You\n")
