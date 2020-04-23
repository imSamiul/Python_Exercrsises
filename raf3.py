def exercise():
    exe = input("Which exercise have you taken?\n")
    return exe


def diet():
    die = input("Which food have you taken?\n")
    return die


j = 1
while j <= 5:
    x = input("What do you want for lock?\n"
              "1 for 'Diet'\n"
              "2 for 'Exercise\n"
              "You can try 5 times.\n")
    if x == "1":
        v = diet()
        break
    elif x == "2":
        exercise()
    else:
        print(x)
        print(f' You have {5 - j} term left')
        j = j + 1

