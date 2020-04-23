guess_number = 18
count = 1
while count <= 9:
    user_guess = int(input("Hey! Guess the number: \n"))
    if user_guess < 18:

        print("Please increase the number and try again. \n")
        print(f'You tried {count}th time.')
        if count < 9:
            print(f'You have {9 - count} chance.')
        else:
            print("Game over. You lose.")
        count = count + 1
    elif user_guess > 18:
        print("Please decrease the number and try again. \n")
        print(f'You tried {count}th time.')
        if count < 9:
            print(f'You have {9 - count} chance.')

        else:
            print("Game over. You lose.")
        count = count + 1
    else:
        print(f'You won in {count}th try. Congratulations!')
        break
