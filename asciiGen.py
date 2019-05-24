# ************************************************************************************************************************
# *                                                                                                                      *
# *   Program: asciiGen.py                                                                                               *
# *                                                                                                                      *
# *   Definition: This program will allow the user to convert images and GIFs into ascii art                             *
# *                                                                                                                      *
# *   Author: Patrick Crowley                                                                                            *
# *                                                                                                                      *
# *   Date: 4/26/19                                                                                                      *
# *                                                                                                                      *
# *   History: [4/23/19] Document created and modified                                                                   *
# *            [4/24/19] Document modified                                                                               *
# *            [4/25/19] Document modified and tested                                                                    *
# *            [4/26/19] Document modified, tested and finished                                                          *
# *                                                                                                                      *
# *                                                                                                                      *
# ************************************************************************************************************************

# Author's Note: I am a Junior in High School, my code is very basic and nowhere near a professional level.
# I apologize for any simple beginner mistakes or any incorrect use of Python.

# ==================================================   IMPORTS   =======================================================
import sys, random, argparse
import numpy
import math
from PIL import Image
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\^`'. "
gscale2 = '@%#*+=-:. '

# ==================================================   FUNCTIONS   =====================================================


# Resizing Function
def average(image):
    im = numpy.array(image)                                        # Image "becomes" an array
    w, h = im.shape                                                # Gets Image shape
    return numpy.average(im.reshape(w * h))                        # Average of resized image in ascii


# Conversion Function
def converter(filename, cols, scale, morelevels):
    global gscale1, gscale2                                        # Declare globals
# Replace filename with the name of image (Make sure the python file and image are in the same location like a folder)
    image = Image.open(filename).convert('L')                      # open image and convert to grayscale
    width, height = image.size[0], image.size[1]                   # store dimensions
    print("input image dims: %d x %d" % (width, height))
    w = width / cols                                               # Width of tile
    h = w / scale                                                  # Tile height based on aspect ratio and scale
    rows = int(height / h)                                         # Number of rows
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
    if cols > w or rows > h:                                       # check if image size is too small
        print("Image too small")
        exit(0)

    aimg = []

    for j in range(rows):                                          # Generate list of dimensions
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        if j == rows - 1:                                          # Correct last tile
            y2 = height
        aimg.append("")                                            # Append an empty string
        for i in range(cols):
            x1 = int(i * w)                                        # Crop image to tile
            x2 = int((i + 1) * w)
            if i == cols - 1:                                      # Correct last tile
                x2 = width
            img = image.crop((x1, y1, x2, y2))                     # Crop image to extract tile
            avg = int(avgerage(img))
            if morelevels:                                         # Look up ascii char
                gsval = gscale1[int((avg * 69) / 255)]
            else:
                gsval = gscale2[int((avg * 9) / 255)]
            aimg[j] += gsval                                       # Append ascii char to string
    return aimg                                                    # Returns image as ascii


# Main Procedure
def main():
    descstr = "This program converts an image into ASCII art."     # Create parser
    parser = argparse.ArgumentParser(description=descstr)
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='moreLevels', action='store_true')
    args = parser.parse_args()
    imgfile = args.imgFile
    outfile = 'output.txt'                                               # Change output name
    if args.outFile:
        outfile = args.outFile
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    cols = 80                                                         # Columns of the ascii image
    if args.cols:
        cols = int(args.cols)
    print('Generating...')
    aimg = covertImageToAscii(imgfile, cols, scale, args.morelevels)  # Convert image to ascii txt
    f = open(outfile, 'w')                                            # Open outfile
    for row in aimg:                                                  # Write to outfile
        f.write(row + '\n')
    f.close()                                                         # Close outfile
    print("ASCII art written to %s" % outfile)


# ====================================================== MAIN ==========================================================
if __name__ == '__main__':
    main()
