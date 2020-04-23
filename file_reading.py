# 1
f = open("harry.txt")
content = f.read()
print("1", content, "\n")
f.close()
# 2
g = open("harry.txt", "r")
# this "r" is by default for reading if it consist or not
content = g.read()
print("2", content, "\n")
g.close()
# 3
h = open("harry.txt", "rb")
# this will print as a binary form
content = h.read()
print("3", content, "\n")
h.close()
# 4
i = open("harry.txt", "rt")
# this will print as a text form which is by default
jaihok = i.read()
print("4", jaihok, "\n")
i.close()
# 5
j = open("harry.txt", "rt")
content = j.read(3)
print("5", content)
# this will print 1st 3 character of the first line
content = j.read(4)
print(content, "\n")
# this will print 4 character after the 1st 3 character
j.close()
# 6
k = open("harry.txt", "rt")
content = k.read(344455)
print("5", content)
# the output will finished form here
content = k.read(4)
print("6", content, "\n")
# there nothing will print after 6 because the count has taken from 1st part
k.close()
# 7
l = open("harry.txt", "rt")
content = l.read()
print("7")
for line in content:
    print("7", line)
print("\n")
# this will print character by character
l.close()
# 8
m = open("harry.txt", "rt")
# content = m.read()
print("8")
for line in m:
    print("8", line, end="")
print("\n")
# this will print line by line
m.close()
# 9
n = open("harry.txt", "rt")
print("9", n.readline())
print("9", n.readline())
# this will print the line after one after
n.close()
# 10
n = open("harry.txt", "rt")
print("10", n.readlines())
print("11", n.readlines())
# this will print the line after one after without making a new line
n.close()