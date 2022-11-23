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

filetype = args[1][-3:len(args[1])]

if (not filetype == 'png' and not filetype == 'jpg' and not filetype == 'jpeg'):
    print(f'Error: Filetype mus be PNG or JPEG. Instead got {filetype}')
    quit()

img = Image.open(args[1])

if (not img):
    print('Error: Could not load image')
    quit()

rows = int(args[2])
cols = int(args[3])
print(rows, cols)
width = int(img.size[0])
height = int(img.size[1])
frameW = int(width / cols)
frameH = int(height / rows)

print(f'Width: {width}, Height: {height}, FW: {frameW}, FH: {frameH}')

new_filename = f'{args[1][0:-4]}_flipped.{filetype}'

def invertFrame(row, col):
    arr = np.array(img)
    row = int(row * frameW)
    col = int(col * frameH)
    
    rowE = int(row+frameW)
    colE = int(col+frameH)

    frame = Image.fromarray(arr[row:rowE, col:colE]).transpose(method=Image.FLIP_LEFT_RIGHT)

    flipped = np.array(frame)

    arr[row:rowE, col:colE] = flipped
  
    return Image.fromarray(arr)

for i in range(rows):
    for j in range(cols):
        img = invertFrame(i, j)



img.save(new_filename)



print('New Image Saved')