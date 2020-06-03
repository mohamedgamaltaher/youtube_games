# Let's import necessary module
import sys  # Requre to exit the game

# Define some global variables
player_1_choice = 'x'
player_2_choice = 'o'
game_draw = 'DRAW'

# Define grid
# We will use list comprehension to create 3 x 3 grid.

grid = [cell for cell in range(9)]

# Let us create a function that display a grid


def display_grid():
    """
    This function will display a grid 
    in a screen
    """

    print(f"{grid[0]}  {grid[1]}  {grid[2]}")
    print(f"{grid[3]}  {grid[4]}  {grid[5]}")
    print(f"{grid[6]}  {grid[7]}  {grid[8]}")


# Lets call display_grid function
display_grid()

# Let's write a function that will check winning condition and
# tie condition of a game


def check_winner():
    """Function that will check the 
    equal rows
    equal cols
    diagonal 
    and draw condition of a game
    """

    # Check the rows
    if grid[0] == grid[1] == grid[2]:
        return grid[0]
    elif grid[3] == grid[4] == grid[5]:
        return grid[3]
    elif grid[6] == grid[7] == grid[8]:
        return grid[6]

    # Check for cols
    elif grid[0] == grid[3] == grid[6]:
        return grid[0]

    elif grid[1] == grid[4] == grid[7]:
        return grid[1]

    elif grid[2] == grid[5] == grid[8]:
        return grid[2]

    # Check for diagonal
    elif grid[2] == grid[4] == grid[6]:
        return grid[2]

    elif grid[0] == grid[4] == grid[8]:
        return grid[2]

    # Check for draw.
    else:
        for cell in grid:
            if isinstance(cell, int):
                # Game is ongoing yet not finised
                # Do nothing
                # just return
                return

        return game_draw


# Let's create a game function that will call
# check_winner function and retun the condition of a game

def game():
    winner = check_winner()

    if winner == 'x':
        print("X: is the winner")
        display_grid()
        sys.exit()

    elif winner == 'o':
        print("O: is the winenr")
        display_grid()
        sys.exit()

    elif winner == game_draw:
        print("Game is draw ")
        sys.exit()


# Not lets create a function that will validate the player input
# And check if the location of the grid are
# already occoupied ask for another input
# the function will be update_grid


def update_grid(choice, location):
    """
    choice: 'x' or 'o'
    location: (0 to 8)
    """

    if location < 0 or location > 9:
        # You could just print and return None
        # I am returning ValueError to ease the debugging process
        raise ValueError("Not a valid location")

    # Check for the occoupied condition of grid cell
    if grid[location] == 'x' or grid[location] == 'o':
        raise ValueError("Location already filled with", grid[location])

    # if none of the condtion matches
    # User input is valid
    else:
        grid[location] = choice

# Now let's create a main function
# that will call the game and update_grid function
# and ask for the player input


def main():
    player_1_location = int(
        input("Player [x] Enter your choice from ( 0 to 8)"))
    # pass player 1 location choice using update_grid function
    update_grid(player_1_choice, player_1_location)

    # After updateing check the winning, loosing or draw condition
    # by calling game function
    game()

    player_2_location = int(
        input("Player [o] Enter your choice from ( 0 to 8)"))
    # pass player 2 location choice using update_grid function
    update_grid(player_2_choice, player_1_location)
