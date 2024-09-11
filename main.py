# Define the number of weights (discs)
NUM_WEIGHTS = 5

# Initialize rods
rod_1 = list(range(NUM_WEIGHTS, 0, -1))  # Full with weights (largest to smallest)
rod_2 = []
rod_3 = []
rod_4 = []

# Dictionary to map rod names to actual lists
rods = {
    '1': rod_1,
    '2': rod_2,
    '3': rod_3,
    '4': rod_4
}

# Function to display the current state of rods
def display_rods():
    print("\nCurrent Rod Status:")
    for i in range(1, 5):
        print(f"Rod {i}: {rods[str(i)]}")
    print()

# Function to move a disc from one rod to another
def move_disc(from_rod, to_rod):
    # Convert input strings to actual lists
    from_stack = rods[from_rod]
    to_stack = rods[to_rod]
    
    # Validate the move
    if len(from_stack) == 0:
        print("\nInvalid move: The source rod is empty!")
        return False
    if len(to_stack) > 0 and from_stack[-1] > to_stack[-1]:
        print("\nInvalid move: You can't place a heavier weight on a lighter one!")
        return False
    
    # Move the disc
    to_stack.append(from_stack.pop())
    print(f"\nMoved disc from Rod {from_rod} to Rod {to_rod}.")
    return True

# Function to check if all weights are moved to any rod other than rod 1
def check_win():
    return len(rod_1) == 0 and (len(rod_2) == NUM_WEIGHTS or len(rod_3) == NUM_WEIGHTS or len(rod_4) == NUM_WEIGHTS)

# Main game loop
def play_game():
    print("Welcome to the 4-Rod Weight Transfer Puzzle!")
    print(f"Your goal is to transfer all weights from Rod 1 to another rod (Rod 2, 3, or 4).")
    print("You can only move one weight at a time, and you cannot place a heavier weight on top of a lighter one.\n")
    
    display_rods()
    
    while True:
        from_rod = input("Enter the rod number to move from (1, 2, 3, 4): ").strip()
        to_rod = input("Enter the rod number to move to (1, 2, 3, 4): ").strip()
        
        # Validate input
        if from_rod not in ['1', '2', '3', '4'] or to_rod not in ['1', '2', '3', '4']:
            print("\nInvalid input! Please enter rod numbers between 1 and 4.")
            continue
        
        if from_rod == to_rod:
            print("\nInvalid move: Source and destination rods are the same!")
            continue
        
        # Try to move the disc
        move_disc(from_rod, to_rod)

        # Reprint rods after every move (valid or invalid)
        display_rods()
        
        # Check if the player has won
        if check_win():
            print("Congratulations! You've successfully transferred all the weights!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
