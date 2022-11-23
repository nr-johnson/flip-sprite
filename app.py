import sys
from os.path import exists
from PIL import Image
import numpy as np

args = sys.argv

if (not len(args) == 4):
    print(f'Error: Expected 3 arguments but received {len(args) - 1}')
    print('Usage: "relative-path-to-file" sprite-rows-count sprite-columns-count')
    quit()

file_exists = exists(args[1])

if (not file_exists):
    print('Error: Invalid file path')
    quit()

img = Image.open(args[1])

if (not img):
    print('Error: Could not load image')
    quit()

rows = int(args[2]) - 1
cols = int(args[3]) - 1

width = int(img.size[0])
height = int(img.size[1])
frameW = width / (rows + 1)
frameH = height / (cols + 1)

print(f'Width: {width}, Height: {height}, FW: {frameW}, FH: {frameH}')

new_filename = f'{args[1][0:-4]}_flipped{args[1][-4:len(args[1])]}'

def invertFrame(col, row):
    arr = np.array(img)
    col = int(col * frameH)
    row = int(row * frameW)
    colE = int(col+frameH)
    rowE = int(row+frameW)

    frame = Image.fromarray(arr[row:rowE, col:colE]).transpose(method=Image.FLIP_LEFT_RIGHT)

    flipped = np.array(frame)

    arr[row:rowE, col:colE] = flipped
  
    return Image.fromarray(arr)

for i in range(rows):
    for j in range(cols):
        img = invertFrame(j, i)

img.save(new_filename)



print('New Image Saved')