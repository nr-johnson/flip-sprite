# Sprite Sheet Flipper

This program is pretty simple.

It takes a sprite sheet and flips each frame horizontally. This allows the use of the same frame references when using a flipped sprite in a game.

## Usage:

The program take three arguments:
* The path to the image to be flipped relative to the program directory
* The number of rows in the sprite sheet
* The number of columns in the sprite sheet

After running the program a new image will be save in the same directory as the original image. The name will be the same as the original but with '_flipped' added.

## Packages Used:
For the program to work both Pillow and Numpy must be installed.
