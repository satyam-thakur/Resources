def bomb_at(i, j):
    # Represent the grid as a list of strings
    grid = [".........",
        ".....X...",
        ".....X...",
        ".....X...",
        "........."
    ]
    # print (grid[0,5])
    # Check if the coordinates are within the grid and if there's an 'X' at that position
    return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 'X'
    

# Solution
grid_length = 9  # Assuming a 9x9 grid based on the example
battleship_parts = []

for i in range(grid_length):
    for j in range(grid_length):
        if bomb_at(i,j):
            battleship_parts.append((i,j))

# Print results
if len(battleship_parts) == 3:
    print(f"Head: {battleship_parts[0]}")
    print(f"Middle: {battleship_parts[1]}")
    print(f"Tail: {battleship_parts[2]}")
else:
    print(f"Found {len(battleship_parts)} battleship parts, expected 3.")


'''
Gridsize = ?
check for each element in grid if there exists a ship
will use function to check the (a, b) position for ship
res will have 3 arguments, display as head middle and tail
'''