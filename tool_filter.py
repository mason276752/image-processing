#!/usr/local/bin/python3
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import sys
import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input image filename",
                    default="photo.jpg")
parser.add_argument("--blur", help="高斯模糊 GaussianBlur(float)",
                    type=float, default=0)  # 高斯模糊
parser.add_argument("--saturation", help="飽和度 Color(float)",
                    type=float, default=1)  # 飽和度
parser.add_argument("--brightness", help="亮度 Brightness(float)",
                    type=float, default=1)  # 亮度
parser.add_argument("--sharpness", help="銳利度 Sharpness(float)",
                    type=float, default=1)  # 銳利度
parser.add_argument("--contrast", help="對比 Contrast(float)",
                    type=float, default=1)  # 對比
parser.add_argument(
    "--output", help="output image filename", default="output.jpg")
args = parser.parse_args()

image = Image.open(args.input)


print("GaussianBlur: ", args.blur)
image = image.filter(ImageFilter.GaussianBlur(args.blur))  # 模糊
# image=image.filter(ImageFilter.CONTOUR)	#輪廓
# image=image.filter(ImageFilter.DETAIL)
# image=image.filter(ImageFilter.EDGE_ENHANCE)	#邊界加強
# image=image.filter(ImageFilter.EDGE_ENHANCE_MORE)	#邊界加強(閥值更大)
# image=image.filter(ImageFilter.EMBOSS)	#浮雕
# image=image.filter(ImageFilter.FIND_EDGES)	#邊界
# image=image.filter(ImageFilter.SMOOTH)	#平滑
# image=image.filter(ImageFilter.SMOOTH_MORE)	#平滑(閥值更大)
# image=image.filter(ImageFilter.SHARPEN)	#銳化

# 亮度
print("Brightness: ", args.brightness)
enh_bri = ImageEnhance.Brightness(image)
brightness = args.brightness
image = enh_bri.enhance(brightness)


# 飽和
print("Saturation: ", args.saturation)
enh_col = ImageEnhance.Color(image)
color = args.saturation
image = enh_col.enhance(color)


# 對比
print("Contrast: ", args.contrast)
enh_con = ImageEnhance.Contrast(image)
contrast = args.contrast
image = enh_con.enhance(contrast)


# 銳度
print("Sharpness: ", args.sharpness)
enh_sha = ImageEnhance.Sharpness(image)
sharpness = args.sharpness
image = enh_sha.enhance(sharpness)
Path("./temp").mkdir(parents=True, exist_ok=True)
image.save("./temp/"+args.output)
