import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def generate_code(width=120, height=30, font_file='Monaco.ttf', font_size=28):
    """
    This function generates a random question.
    """

    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_file, font_size)

    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    number = str(num1) + str(num2)

    draw.text((0, 0), number, (0, 0, 0), font=font)

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img