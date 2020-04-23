f = open("harry.txt")
f.seek(11)
print(f.tell())
print(f.readline())

# f.seek(10)
print(f.readline())
# print(f.tell())
f.close()
