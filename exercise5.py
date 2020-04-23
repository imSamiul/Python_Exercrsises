from Tools.scripts.mkreal import join


def getdate():
    import datetime
    x = str(datetime.datetime.now())
    return x


lock_or_retrieve = input("Do you want to lock or retrieve?\n")
if lock_or_retrieve == "lock":
    person = input("Which one do you want to lock?\n"
                   "1 for Jubayer\n"
                   "2 for Anamul\n"
                   "3 for Shrabon\n")
    if person == "1":
        diet_or_exercise = (input("What do you want for lock?\n"
                                  "1 for Diet\n"
                                  "2 for Exercise\n"))
        if diet_or_exercise == "1":
            eat = input("What do you eat?\n")
            with open("Jubayer.txt", "a") as f:
                a = "[" + getdate() + "]" + " " + eat + "\n"
                f.write(a)
        else:
            exercise = input("Which exercise do you take?\n")
            with open("JubayerExercise.txt", "a") as f:
                a = "[" + getdate() + "]" + " " + exercise + "\n"
                f.write(a)

    elif person == "2":
        diet_or_exercise = (input("What do you want for lock?\n"
                                  "1 for Diet\n"
                                  "2 for Exercise\n"))
        if diet_or_exercise == "1":
            eat = input("What do you eat?\n")
            with open("Anamul.txt", "a") as f:
                a = "[" + getdate() + "]" + " " + eat + "\n"
                f.write(a)
        else:
            exercise = input("Which exercise do you take?\n")
            with open("AnamulExercise.txt", "a") as f:
                a = "[" + getdate() + "]" + " " + exercise + "\n"
                f.write(a)
    elif person == "3":
        diet_or_exercise = (input("What do you want for lock?\n"
                                  "1 for Diet\n"
                                  "2 for Exercise\n"))
        if diet_or_exercise == "1":
            eat = input("What do you eat?\n")
            with open("Shrabon.txt", "a") as f:
                a = "[" + getdate() + "]" + " " + eat + "\n"
                f.write(a)
        else:
            exercise = input("Which exercise do you take?\n")
            with open("ShrabonExercise.txt", "a") as f:
                a = "[" + getdate() + "]" + " " + exercise + "\n"
                f.write(a)
elif lock_or_retrieve == "retrieve":
    person = input("Which one do you want to retrieve?\n"
                   "1 for Jubayer\n"
                   "2 for Anamul\n"
                   "3 for Shrabon\n")
    if person == "1":
        diet_or_exercise = (input("What do you want for retrieve?\n"
                                  "1 for Diet\n"
                                  "2 for Exercise\n"))
        if diet_or_exercise == "1":
            with open("Jubayer.txt") as f:
                read = f.read()
                print(read, "\n")
        else:
            with open("JubayerExercise.txt") as f:
                read = f.read()
                print(read, "\n")
    elif person == "2":
        diet_or_exercise = (input("What do you want for retrieve?\n"
                                  "1 for Diet\n"
                                  "2 for Exercise\n"))
        if diet_or_exercise == "1":
            with open("Anamul.txt") as f:
                read = f.read()
                print(read, "\n")
        else:
            with open("AnamulExercise.txt") as f:
                read = f.read()
                print(read, "\n")
    elif person == "3":
        diet_or_exercise = (input("What do you want for retrieve?\n"
                                  "1 for Diet\n"
                                  "2 for Exercise\n"))
        if diet_or_exercise == "1":
            with open("Shrabon.txt") as f:
                read = f.read()
                print(read, "\n")
        else:
            with open("ShrabonExercise.txt") as f:
                read = f.read()
                print(read, "\n")
else:
    print("check the keyword again!")

