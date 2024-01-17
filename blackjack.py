import random

# List of opponents
opponents = ["Jack", "John", "Jill", "Hill"]
# Randomly select an opponent
opponent = random.choice(opponents)

# Display game title
print("=====================")
print("   Black Jack V1.0")
print("    Made by Hamza")
print("=====================\n")

# Display the opponent's name
print(f"Opponent name: {opponent}")

# Initialize player and opponent cards
no_player_cards = sum(random.randint(1, 10) for _ in range(2))
no_opponent_cards = sum(random.randint(1, 10) for _ in range(2))


# Function to display cards
def display_cards():
    print("=====================")
    print(f"{opponent}: {no_opponent_cards}")
    print(f"Player: {no_player_cards}")
    print("=====================")


# Display initial cards
display_cards()

# Initialize player and opponent stand flags
player_stand = False
opponent_stand = False

# Main game loop
while True:
    # Player's turn
    if not player_stand:
        player_choice = input("1. Hit\n2. Stand\n> ")
        if player_choice == "2":
            player_stand = True
        elif player_choice == "1":
            no_player_cards += random.randint(1, 10)

    # Opponent's turn
    if not opponent_stand:
        opponent_choice = random.randint(1, 2)
        if opponent_choice == 2:
            opponent_stand = True
        elif opponent_choice == 1:
            no_opponent_cards += random.randint(1, 10)

    # Display current cards
    display_cards()

    # Check for game-ending conditions
    if no_player_cards > 21 or no_opponent_cards > 21 or (player_stand and opponent_stand):
        break

# Display game over message
print("Game Over!")
display_cards()

# Determine and print the winner
if no_player_cards > 21:
    print(f"{opponent} wins! Player busted.")
elif no_opponent_cards > 21:
    print(f"Player wins! {opponent} busted.")
elif no_player_cards == no_opponent_cards:
    print("It's a draw!")
elif no_player_cards > no_opponent_cards:
    print("Player wins!")
else:
    print(f"{opponent} wins!")
