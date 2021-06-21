#!/usr/local/bin/python3
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys,math
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--mode", help="image mode",type=int,default=0)
parser.add_argument("--bgcolor", help="background color",nargs='+',type=int,default=(255,255,255,255))
parser.add_argument("--bgimage", help="background image",type=str)
parser.add_argument("--borderwitdh", help="border witdh",type=int,default=30)
parser.add_argument("--border", help="border color",nargs='+',type=int)
parser.add_argument("--fontcolor", help="font color",nargs='+',type=int,default=(0,0,0,255))
parser.add_argument("--fontfamily", help="fontfamily",type=str,default="fontfamily/wqy-microhei.ttc")
parser.add_argument("--textalign", help="font color",type=str,default="left")
parser.add_argument("--footer", help="footer",type=str, default="")
parser.add_argument("--resize", help="resize",type=int)
parser.add_argument("--output", help="output")
args = parser.parse_args()

args.bgcolor= tuple(args.bgcolor) if args.bgcolor != None else None
args.border=tuple(args.border) if args.border != None else None
args.fontcolor=tuple(args.fontcolor) if args.fontcolor != None else None

# font setting
font = ImageFont.truetype(args.fontfamily,200)
s="                                              \n" # text center position 

if args.mode == 0:
    # mod 0
    wh=(3000,3000)
    output = args.output or 'out3030.png'
elif args.mode == 1:
    # mod 1
    wh=(3000,1500)
    output = args.output or 'out3015.png'
elif args.mode == 2:
    # mod 2
    wh=(3000,2000)
    output = args.output or 'out3020.png'
elif args.mode == 3:
    # mod 3
    s="                 \n" # text center position 
    wh=(1500,3000)
    output = args.output or 'out1530.png'
elif args.mode == 4:
    # mod 4
    s="                           \n" # text center position 
    wh=(2000,3000)
    output = args.output or 'out2030.png'
elif args.mode == 5:
    # mod 5
    s="                 \n" # text center position 
    wh=(1500,1500)
    output = args.output or 'out1515.png'

# new image
target = Image.new(mode='RGBA', size=wh,color=args.bgcolor)
width, height = target.size
draw = ImageDraw.Draw(target)

# background image
print("background image: " if args.bgimage else "background color:",args.bgimage or args.bgcolor)
if args.bgimage != None:
    fromfile = Image.open(args.bgimage)
    fromfile=fromfile.resize(wh)
    target.paste(fromfile,(0,0))

# border
if args.border != None:
    print("border color: ",args.border,"witdh",args.borderwitdh)
    draw.rectangle((150,150,width-150,height-150),outline=args.border,width=args.borderwitdh)


# print text
print("font color: ",args.fontcolor)
print("fontfamily: ",args.fontfamily)
print("text align: ",args.textalign)
print(output,"text input (double enter next step): ")
n=0
enter_count=0
for line in sys.stdin:
    s+=line
    if '' == line.rstrip():
        enter_count+=1
        if enter_count == 2:
            break
        else:
            continue
    else:
        enter_count=0
    # draw.text((300, 300+n*200), line, fill=args.fontcolor,font=font)
    # n+=1
draw.text((300, 100), s, fill=args.fontcolor,font=font, align=args.textalign)
draw.text((300, height-500), args.footer, fill=args.fontcolor,font=font)
print("footer: ",args.footer)

# resize
if args.resize != None:
    print("resize: ",args.resize)
    if width > height:
        target=target.resize((args.resize,round(height*(args.resize/width))))
    else:
        target=target.resize((round(width*(args.resize/height)),args.resize))

Path("./output").mkdir(parents=True, exist_ok=True)
print("output: ", "./output/"+output, target.size)
target.save("./output/"+output)