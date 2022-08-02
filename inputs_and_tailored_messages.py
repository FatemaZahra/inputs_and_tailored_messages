def user_details():
    name = input("Please enter your name")
    print(f"Hello {name}, welcome aboard!")

    height = input("Please enter your height")
    print(f"Your height is: {height}")

    fav_colour = input("Please enter your favourite colour")
    print(f"Your favourite colour is: {fav_colour}")

    ss_animal = input("Please enter your secret spirited animal")
    print(f"The first letter of your secret spirited animal is {ss_animal[0]} and the last letter of your spirited animal is {ss_animal[-1]}. The number of character it contains {len(ss_animal)}")

    guess_ss_animal = input("Please guess the spirited animal")
    if guess_ss_animal == ss_animal:
        print("OMG how did you know?! :D")
    else:
        print("Better luck next time!")


user_details()