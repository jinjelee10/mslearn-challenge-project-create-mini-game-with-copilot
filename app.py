import random

def computerChoice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def determineWinner(user_input, computer_input):
    if user_input == computer_input:
        return "It's a tie!"
    elif user_input == "rock":
        if computer_input == "paper":
            return "Computer wins!"
        else:
            return "User wins!"
    elif user_input == "paper":
        if computer_input == "scissors":
            return "Computer wins!"
        else:
            return "User wins!"
    elif user_input == "scissors":
        if computer_input == "rock":
            return "Computer wins!"
        else:
            return "User wins!"

def initialise():
    valid_options = ["rock", "paper", "scissors"]
    rounds = 0
    score = 0

    while True:
        while True:
            user_input = input("Please enter your option (rock, paper, or scissors): ").lower()
            if user_input in valid_options:
                break
            else:
                print("Invalid option. Please enter either 'rock', 'paper', or 'scissors'.")

        computer_input = computerChoice()
        print(f"Computer chose: {computer_input}")
        winner = determineWinner(user_input, computer_input)
        print(winner)

        rounds += 1
        if winner == "User wins!":
            score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Game over! You played {rounds} rounds and won {score} rounds.")
            break
def main():
    initialise()

if __name__ == "__main__":
    main()