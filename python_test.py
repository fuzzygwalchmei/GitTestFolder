"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import os

#Set window starting position
x = 300; y = 300; os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# Define some colors
COLOURCODES = {"BLACK":(0,0,0), "WHITE": (255,255,255), "RED":(255,0,0), "GREEN":(0,255,0), "BLUE":(0,0,255), "GREY":(128,128,128)}

# Define lists for movement and actions
MOVEKEYS = {pygame.K_DOWN:(1,0), pygame.K_UP:(-1,0), pygame.K_LEFT:(0,-1), pygame.K_RIGHT:(0,1)}

# This sets the WIDTH and HEIGHT of each grid location # This sets the margin between each cell # This sets the number of rows and columns required
WIDTH = 15; HEIGHT = 15; MARGIN = 1; ROWS = 30; COLUMNS = 45

# Calculate the required screensize
SCR_WIDTH = (WIDTH + MARGIN) * COLUMNS + MARGIN
SCR_HEIGHT = (HEIGHT + MARGIN) * ROWS + MARGIN

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(ROWS):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(0)  # Append a cell
        if (row == 0) or (column == 0) or (row == ROWS-1) or (column == COLUMNS-1):
            grid[row][column] = '#'



# Set row 1, cell 5 to one. (Remember rows and column numbers start at zero.)
X_coord = 1; y_coord = 5; grid[X_coord][y_coord] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [SCR_WIDTH, SCR_HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key in MOVEKEYS:
                test_X_coord = X_coord; test_y_coord=y_coord; test_X_coord += MOVEKEYS[event.key][0]; test_y_coord += MOVEKEYS[event.key][1]
                if grid[test_X_coord][test_y_coord] != '#':
                    grid[X_coord][y_coord] = 0; X_coord = test_X_coord;y_coord=test_y_coord
            grid[X_coord][y_coord] = 1

            # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(ROWS):
        for column in range(COLUMNS):
            color = COLOURCODES["WHITE"]
            if grid[row][column] == '#': color = COLOURCODES["GREY"]
            elif grid[row][column] == 1: color = COLOURCODES["GREEN"]
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
