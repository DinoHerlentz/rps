import random

random_rps = ["rock", "paper", "scissors"]
rps = random.choice(random_rps)

while True:
    # print(rps)
    choice = input("Enter your rps choice : ")
    
    if choice not in random_rps:
        print("That is not a valid option! Please choose between rock, paper, scissors!")
        break
    else:
        if choice == rps:
            print(f"Tie! We both picked {choice}.")
        elif choice == "rock":
            if rps == "paper":
                print(f"I win! I picked {rps} and you picked {choice}.")
            elif rps == "scissors":
                print(f"You win! I picked {rps} and you picked {choice}.")
        elif choice == "paper":
            if rps == "rock":
                print(f"You win! I picked {rps} and you picked {choice}.")
            elif rps == "scissors":
                print(f"I win! I picked {rps} and you picked {choice}.")
        elif choice == "scissors":
            if rps == "rock":
                print(f"I win! I picked {rps} and you picked {choice}.")
            elif rps == "paper":
                print(f"You win! I picked {rps} and you picked {choice}.")
    
    play_again = input("Play again? (yes/no) : ")
    
    if play_again == "no":
        break
    elif play_again != "yes":
        print("Invalid option!")
        break
