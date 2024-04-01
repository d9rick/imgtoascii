import math
from PIL import Image
import sys

# define the characters array
characters = list("@&%QWNM0gB$#DR8mHXKAUbGOpV4d9h6PkqwSE2]ayjxY5Zoen[ult13If}\C{\iF|(7J)vTLs?z/*cr!+<>;=^,_:'-.` ")

# get image name
print("Enter the path to your image: ")
path = input()

# open image
try:
    image = Image.open(path)
except FileNotFoundError as e:
    print(e)
    print("File not found! Terminating!")
    exit()

# extract pixels
pixels = image.load()
width, height = image.size

# foreach pixel add text of "same" brightness
output = ""
for i in range(height):
    for j in range(width):
        # luminance function from https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
        brightness = (0.2126*pixels[j, i][0] + 0.7152*pixels[j, i][1] + 0.0722*pixels[j, i][2])
        
        # normalize brightness & get array index
        brightness = brightness / 255
        char_index = math.floor(brightness * len(characters))        
        
        output += characters[char_index]
    output += '\n'

# create file
file = open("output.txt", "w")
file.write(output)
file.close()