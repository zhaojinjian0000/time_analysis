import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import argparse
def image_write_text(img,text, left, top, textColor, textSize):
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype(r'HGY3_CNKI.TTF', textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return img
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='A wallpaper generate tool for IDP learning.')
    parser.add_argument('--wallpaper', type=str,default=r"wallpaper.jpg", help='input wallpaper picture path')
    parser.add_argument('--chartpng', type=str,required=True, nargs=3,help='input hart pictures paths')
    parser.add_argument('--output', type=str,default=r"wallpaper_new.jpg", help='output wallpaper picture path')
    args = parser.parse_args()
    img = Image.open(args.wallpaper)
    
    try:
        with open("wallpaper_text.txt",'r',encoding='utf-8')as f:
            img = image_write_text(img, f.read(), img.size[0]//15,img.size[1]*4//6,(28,128,179),60)
    except Exception as e:
        import traceback
        traceback.print_exc()
    height_ratio = 0.1
    weight_ratio = (1-0.618)/1.5


    weight = int(img.size[0]*weight_ratio)
    height = img.size[1]/(4*height_ratio+3)
    gap = int(height_ratio*height)
    height = int(height)
    r'pics/20210305-zjj-efficience_pie_chart.png'
    r'pics/20210305-zjj-energy_trend.png'
    r'pics/20210305-zjj-time_matrix_pie_chart.png'
    img_1 = Image.open(args.chartpng[0]).resize((weight,height))
    img_2 = Image.open(args.chartpng[1]).resize((weight,height))
    img_3 = Image.open(args.chartpng[2]).resize((weight,height))
    img.paste(img_1,(int(img.size[0]*(0.809-weight_ratio/2)),gap))
    img.paste(img_2,(int(img.size[0]*(0.809-weight_ratio/2)),gap+(gap+height)))
    img.paste(img_3,(int(img.size[0]*(0.809-weight_ratio/2)),gap+(gap+height)*2))

    img.save(args.output)
    print('already generated')

    