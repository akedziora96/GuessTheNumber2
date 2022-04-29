def guess_the_number_2():

    """Function is a simple game where  user think in the range 1-1000 and the computer will keep guessing.
       He will do up to a maximum of 10 moves and the player will give hints "too big", "too small" or YOU WON."""

    print("Think a number between 1 and 1000.I will guess it im max 10 steps. Let's play !")
    min, max = 0, 1000

    try_number = 1

    while try_number <= 10:

        guess = int((max - min) / 2) + min
        print(f"I guess {guess}")

        player_input = input("Choose answer: 1 - 'too big', 2 - 'too small' or 3 - 'you guessed': ")
        if player_input not in '123':
            print("Hey don't cheat")
            continue

        if player_input == '3':
            print('I WON!')
            break
        else:
            if player_input == '1':
                max = guess
            elif player_input == '2':
                min = guess

            try_number += 1
            continue

    if try_number <= 10:
        print(f'Computer won in {try_number} steps.')
    else:
        print(f'Computer lost a game.')


guess_the_number_2()
