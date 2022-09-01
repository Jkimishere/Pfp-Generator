
from os import path
from PIL import Image, ImageOps
from random import choice, randint

def main():
    file_location = input('Input your file location')
    if not path.isdir(file_location.strip()):  
        print('Invalid location(file directory)')
        main()
    else:
        generate_image(file_location)

def generate_image(path):
    pfp = Image.new(mode="RGB", size=(4,8), color=(255, 255, 255));
    temp = Image.new(mode="RGB", size=(8,8), color=(255, 255, 255));
    color = generate_color()
    for x in range(4):
        pfp.putpixel([randint(0,3), randint(0,7)], color)

    

    temp.paste(pfp)
    temp.paste(ImageOps.mirror(pfp), (4,0))
    big = temp.resize((1024,1024),resample=Image.Resampling.BOX)
    big.save(path.strip() + '\\pfp.png')
def generate_color():
    return choice([(87, 150, 250),(128, 227, 95), (202, 95, 232),(235, 96, 108),(235, 175, 96)])


main()