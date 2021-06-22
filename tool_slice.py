#!/usr/local/bin/python3
from PIL import Image
import argparse
import math
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input image filename",
                    default="photo.jpg")
parser.add_argument("--output", help="output image filename",
                    default="output.jpeg")
parser.add_argument("--width-proportion", help="width slice proportion",
                    nargs='+', type=int, default=[2, 1])
parser.add_argument("--height-proportion",
                    help="height slice proportion", nargs='+', type=int, default=[1])

args = parser.parse_args()
print("width proportion:", ':'.join(map(str, args.width_proportion)))
print("height proportion:", ':'.join(map(str, args.height_proportion)))

img = Image.open(args.input)
width, height = img.size
widthSlice = int(width/math.fsum(args.width_proportion))
heightSlice = int(height/math.fsum(args.height_proportion))

for i, wvalue in enumerate(args.width_proportion):
    for j, hvalue in enumerate(args.height_proportion):
        new_img = Image.new(mode='RGB', size=(
            widthSlice*wvalue, heightSlice*hvalue))
        new_img.paste(img.crop((math.fsum(args.width_proportion[0:i])*widthSlice, math.fsum(args.height_proportion[0:j])*heightSlice, math.fsum(
            args.width_proportion[0:i+1])*widthSlice, math.fsum(args.height_proportion[0:j+1])*heightSlice)), (0, 0))
        outfilename = str(i)+","+str(j)+args.output
        Path("./temp").mkdir(parents=True, exist_ok=True)
        new_img.save("./temp/"+outfilename)
        print("output image:", "./temp/"+outfilename)
