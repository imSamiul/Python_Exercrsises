star_input = int(input("How Many Row You Want To Print\n"))
direct_reverse = int(input("Put the value "
                           "1 for direct"
                           "0 for reverse\n"))
if direct_reverse == 1:
    star = 1
    while star <= star_input:
        output = "*" * star
        print(output)
        star = star + 1
else:
    star = star_input
    while star <= star_input:
        output = "*" * star
        print(output)
        star = star - 1
        if star == 0:
            break
