print("Think of a fruit.")
input("Press Enter when you have one in mind...")
red = input("Is it a red fruit? (yes/no): ").strip().lower()

if red == "yes":
    small = input("Is it a really small fruit, (berry size)? (yes/no): ").strip().lower()
    if small == "yes":
        seed = input("Does it have edible seeds? (yes/no): ").strip().lower()
        if seed == "yes":
            strawberry = input("Is your fruit a strawberry? (yes/no): ").strip().lower()
            if strawberry == "yes":
                print("Yay! I guessed it right.")
            elif strawberry == "no":
                print("Hmm, I give up. What fruit were you thinking of?")
            else:
                print("Please answer 'yes' or 'no'.")
        elif seed == "no":
            cherry = input("Is your fruit a cherry? (yes/no): ").strip().lower()
            if cherry == "yes":
                print("Yay! I guessed it right.")
            elif cherry == "no":
                print("Hmm, I give up. What fruit were you thinking of?")
            else:
                print("Please answer 'yes' or 'no'.")
        else:
            print("Please answer 'yes' or 'no'.")
    elif small == "no":
        big = input("Is it a big fruit, about melon size? (yes/no): ").strip().lower()
        if big == "yes":
            watermelon = input("Is your fruit a watermelon? (yes/no): ").strip().lower()
            if watermelon == "yes":
                print("Yay! I guessed it right.")
            elif watermelon == "no":
                print("Hmm, I give up. What fruit were you thinking of?")
            else:
                print("Please answer 'yes' or 'no'.")
        elif big == "no":
            seeds = input("Hmm, does it have seeds? (yes/no): ").strip().lower()
            if seeds == "yes":
                apple = input("Is your fruit an apple? (yes/no): ").strip().lower()
                if apple == "yes":
                    print("Yay! I guessed it right.")
                elif apple == "no":
                    print("Hmm, I give up. What fruit were you thinking of?")
                else:
                    print("Please answer 'yes' or 'no'.")
            elif seeds == "no":
                raspberry = input("Is your fruit a raspberry? (yes/no): ").strip().lower()
                if raspberry == "yes":
                    print("Yay! I guessed it right.")
                elif raspberry == "no":
                    print("Hmm, I give up. What fruit were you thinking of?")
                else:
                    print("Please answer 'yes' or 'no'.")
            else:
                print("Please answer 'yes' or 'no'.")
        else:
            print("Please answer 'yes' or 'no'.")
    else:
        print("Please answer 'yes' or 'no'.")
elif red == "no":
    berry = input("Is your fruit a berry? (yes/no): ").strip().lower()
    if berry == "yes":
        blue = input("Is your berry blue? (yes/no): ").strip().lower()
        if blue == "yes":
            blueberry = input("Is your fruit a blueberry? (yes/no): ").strip().lower()
            if blueberry == "yes":
                print("Yay! I guessed it right.")
            elif blueberry == "no":
                print("Hmm, I give up. What fruit were you thinking of?")
            else:
                print("Please answer 'yes' or 'no'.")
        elif blue == "no":
            blackberry = input("Is your fruit a blackberry? (yes/no): ").strip().lower()
            if blackberry == "yes":
                print("Yay! I guessed it right.")
            elif blackberry == "no":
                print("Hmm, I give up. What fruit were you thinking of?")
            else:
                print("Please answer 'yes' or 'no'.")
    elif berry == "no":
        tropical = input("Is your fruit a tropical fruit? (yes/no): ").strip().lower()
        if tropical == "yes":
            melon = input("Is your fruit a melon? (yes/no): ").strip().lower()
            if melon == "yes":
                cantaloupe = input("Is your fruit a cantaloupe? (yes/no): ").strip().lower()
                if cantaloupe == "yes":
                    print("Yay! I guessed it right.")
                elif cantaloupe == "no":
                    print("Hmm, I give up. What fruit were you thinking of?")
                else:
                    print("Please answer 'yes' or 'no'.")
            elif melon == "no":
                yellow = input("Is your fruit yellow? (yes/no): ").strip().lower()
                if yellow == "yes":
                    sour = input("Is it kind of sour? (yes/no): ").strip().lower()
                    if sour == "yes":
                        pineapple = input("Is your fruit a pineapple? (yes/no): ").strip().lower()
                        if pineapple == "yes":
                            print("Yay! I guessed it right.")
                        elif pineapple == "no":
                            print("Hmm, I give up. What fruit were you thinking of?")
                        else:
                            print("Please answer 'yes' or 'no'.")
                    elif sour == "no":
                        banana = input("Is your fruit a banana? (yes/no): ").strip().lower()
                        if banana == "yes":
                            print("Yay! I guessed it right.")
                        elif banana == "no":
                            print("Hmm, I give up. What fruit were you thinking of?")
                        else:
                            print("Please answer 'yes' or 'no'.")
                    else:
                        print("Please answer 'yes' or 'no'.")
                elif yellow == "no":
                    mango = input("Is your fruit a mango? (yes/no): ").strip().lower()
                    if mango == "yes":
                        print("Yay! I guessed it right.")
                    elif mango == "no":
                        print("Hmm, I give up. What fruit were you thinking of?")
                    else:
                        print("Please answer 'yes' or 'no'.")
                else:
                    print("Please answer 'yes' or 'no'.")
        elif tropical == "no":
            citrus = input("Is your fruit a citrus fruit? (yes/no): ").strip().lower()
            if citrus == "yes":
                orange = input("Is your fruit an orange? (yes/no): ").strip().lower()
                if orange == "yes":
                    print("Yay! I guessed it right.")
                elif orange == "no":
                    lemon = input("Is your fruit a lemon? (yes/no): ").strip().lower()
                    if lemon == "yes":
                        print("Yay! I guessed it right.")
                    elif lemon == "no":
                        print("Hmm, I give up. What fruit were you thinking of?")
                    else:
                        print("Please answer 'yes' or 'no'.")
                else:
                    print("Please answer 'yes' or 'no'.")
            elif citrus == "no":
                grape = input("Is your fruit a grape? (yes/no): ").strip().lower()
                if grape == "yes":
                    print("Yay! I guessed it right.")
                elif grape == "no":
                    print("Hmm, I give up. What fruit were you thinking of?")
                else:
                    print("Please answer 'yes' or 'no'.")
            else:
                print("Please answer 'yes' or 'no'.")
        else:
            print("Please answer 'yes' or 'no'.")
    else:
        print("Please answer 'yes' or 'no'.")
else:
    print("Please answer 'yes' or 'no'.")




































