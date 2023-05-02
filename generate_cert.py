""" # Python code to generate certificates from a list of names
    # Author : ijas <ijas.dev>
    # Date : 23 June 2020
"""

from PIL import Image, ImageFont, ImageDraw
import pandas as pd
FONT_FILE = ImageFont.truetype(r'Arimo-Italic-VariableFont_wght.ttf', 90)
FONT_COLOR = "#000000"
WIDTH, HEIGHT = 970, 778


def make_cert(name):
    """function to generate certificate"""
    image_source = Image.open(r'certificate.jpg')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text((WIDTH-name_width/2, HEIGHT-name_height/2), name, fill=FONT_COLOR, font=FONT_FILE)
    image_source.save("./out/" + name+".jpg")
    # print('printing certificate of: '+name)


# names = ['Natasha Romanova']
names=[' ',' ']
# data=pd.read_excel('HACKS Registration.xlsx')
# names = list(data.Team_Leader_Name)
for x in names:
    make_cert(x)
