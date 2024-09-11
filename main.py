# Customize the number of weights (discs) and rods
NUM_WEIGHTS = 5
NUM_RODS = 4

# Initialize rods dynamically based on NUM_RODS
rods = {str(i): [] for i in range(1, NUM_RODS + 1)}
rods['1'] = list(range(NUM_WEIGHTS, 0, -1))  # Fill first rod with weights (largest to smallest)

# Function to display the current state of rods
def display_rods():
    print("\nCurrent Rod Status:")
    for i in range(1, NUM_RODS + 1):
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

def check_win():
    return len(rods['1']) == 0 and len(rods[str(NUM_RODS)]) == NUM_WEIGHTS

def play_game():
    print(f"Welcome to the {NUM_RODS}-Rod Weight Transfer Puzzle!")
    print(f"Your goal is to transfer all {NUM_WEIGHTS} weights from Rod 1 to Rod {NUM_RODS}.")
    print("You can only move one weight at a time, and you cannot place a heavier weight on top of a lighter one.\n")
    
    display_rods()
    move_count = 0
    
    while True:
        from_rod = input(f"Enter the rod number to move from (1 to {NUM_RODS}): ").strip()
        to_rod = input(f"Enter the rod number to move to (1 to {NUM_RODS}): ").strip()

        # Validate input
        if from_rod not in rods or to_rod not in rods:
            print(f"\nInvalid input! Please enter rod numbers between 1 and {NUM_RODS}.")
        elif from_rod == to_rod:
            print("\nInvalid move: Source and destination rods are the same!")
        elif move_disc(from_rod, to_rod):
                move_count += 1

        # Always display the rods after each move attempt, EVEN if the input is invalid, it DOZENA matter
        display_rods()
        print(f"Total moves: {move_count}\n")

        if check_win():
            print(f"Congratulations! You've successfully transferred all the weights in {move_count} moves!")
            break

if __name__ == "__main__":
    play_game()
