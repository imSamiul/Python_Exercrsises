def getdate():
    import datetime
    y = str(datetime.datetime.now())
    return y


def exercise():
    exe = input("Which exercise have you taken?\n")
    return exe


def diet():
    die = input("Which food have you taken?\n")
    return die


def person():
    perso = str(input("Which one do you want to lock?\n"
                      "1 for Jubayer\n"
                      "2 for Anamul\n"
                      "3 for Shrabon\n"))
    return perso


i = 1
while i <= 5:
    per2 = person()
    if per2 == "1":
        j = 1
        while j <= 5:
            x = input("What do you want for lock?\n"
                      "1 for 'Diet'\n"
                      "2 for 'Exercise\n")
            if x == "1":
                v = diet()
                with open("Jubayer.txt", "a") as f:
                    a = "[" + getdate() + "]" + " " + v + "\n"
                    f.write(a)
            elif x == "2":
                exercise()
            else:
                print(f' You have {5 - j} term left')
                j = j + 1
        break
    else:
        print(f'You Failed!😒\n'
              f'You have {5 - i} chance')
        i = i + 1

