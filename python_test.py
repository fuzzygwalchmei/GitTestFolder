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
x = 100
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 15
HEIGHT = 15

# This sets the margin between each cell
MARGIN = 1

# This sets the number of rows and columns required
ROWS = 30
COLUMNS = 45

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



# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
X_coord = 1
y_coord = 5
grid[X_coord][y_coord] = 1


#Declare function for movement
def Move_Cursor(keystroke):
    if keystroke == pygame.K_ESCAPE:
        done = True
    elif keystroke == pygame.K_UP:
        X_coord -= 1
        grid[X_coord][y_coord] = 1
    elif keystroke == pygame.K_DOWN:
        X_coord += 1
        grid[X_coord][y_coord] = 1
    elif keystroke == pygame.K_LEFT:
        y_coord -= 1
        grid[X_coord][y_coord] = 1
    elif keystroke == pygame.K_RIGHT:
        y_coord += 1
        grid[X_coord][y_coord] = 1

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
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            # User clicks the mouse. Get the position
#            pos = pygame.mouse.get_pos()
#            # Change the x/y screen coordinates to grid coordinates
#            column = pos[0] // (WIDTH + MARGIN)
#            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
#            grid[row][column] = 1
#            print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_UP:
                X_coord -= 1
            elif event.key == pygame.K_DOWN:
                X_coord += 1
            elif event.key == pygame.K_LEFT:
                y_coord -= 1
            elif event.key == pygame.K_RIGHT:
                y_coord += 1
            grid[X_coord][y_coord] = 1



            # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(ROWS):
        for column in range(COLUMNS):
            color = WHITE
            if grid[row][column] == '#':
                color = GREY
            elif grid[row][column] == 1:
                color = GREEN
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
