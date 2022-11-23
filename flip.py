import sys
from os.path import exists
from PIL import Image
import numpy as np

# System arguments
args = sys.argv

# Verifies that the correct number of arguments were provided
if (not len(args) == 4):
    print(f'Error: Expected 3 arguments but received {len(args) - 1}')
    print('Usage: "relative-path-to-file" sprite-rows-count sprite-columns-count')
    quit()

# Verifies that the image provided exists
file_exists = exists(args[1])
if (not file_exists):
    print('Error: Invalid file path')
    quit()

# Image fileype
filetype = args[1][-3:len(args[1])]

# Verifies that the file is an image
if (not filetype == 'png' and not filetype == 'jpg' and not filetype == 'jpeg'):
    print(f'Error: Filetype mus be PNG or JPEG. Instead got {filetype}')
    quit()

# Add image data to variable
img = Image.open(args[1])

# Sends error if image could not be loaded.
if (not img):
    print('Error: Could not load image')
    quit()

# Variables to be used when flipping image
# converts provided row and column arguments to integers
rows = int(args[2])
cols = int(args[3])

# The height and width of the image
width = int(img.size[0])
height = int(img.size[1])

# The height and with of each frame
frameW = int(width / cols)
frameH = int(height / rows)

# Prints image data to the user
print(f'Width: {width}, Height: {height}, FW: {frameW}, FH: {frameH} Count: {rows * cols}')

# Adds new filename/path to a variable
new_filename = f'{args[1][0:-4]}_flipped.{filetype}'

# Function to flip a frame
def invertFrame(row, col):
    # Converts image to array
    arr = np.array(img)

    # Location of frame start point within the array
    row = int(row * frameW)
    col = int(col * frameH)
    
    # Location of frame end point within the array
    rowE = int(row+frameW)
    colE = int(col+frameH)

    # Converts the frame to an image and flips it
    frame = Image.fromarray(arr[row:rowE, col:colE]).transpose(method=Image.FLIP_LEFT_RIGHT)

    # Takes the new flipped image and reconverts it to an array.
    flipped = np.array(frame)

    # Adds flipped array to original image array
    arr[row:rowE, col:colE] = flipped
    
    # Converts the array back to an image and returns it.
    return Image.fromarray(arr)

# For each frame, replace the image with the frame flipped.
for i in range(rows):
    for j in range(cols):
        img = invertFrame(i, j)

# Saves the new image
img.save(new_filename)
print('New Image Saved')