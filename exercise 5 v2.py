def diet_or_exercise():
    f = 1
    while f <= 5:
        x = input("What do you want for lock?\n"
                  "1 for Diet\n"
                  "2 for Exercise\n")
        if x == "1":
            eat = input("What do you eat?\n")
            return eat
        else:
            print(x)
            print(f' You have {5 - f} term left')
            f = f + 1

    # i = 1
    # while i < 5:


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
        v = diet_or_exercise()

        break
    else:
        print(f'Try again'
              f'You have {5 - i} chance')
        i = i + 1
print(v)
