from django.http import HttpResponse
from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO

def display_final_result(self, text, font_size, font_red, font_green, font_blue, farm, server_id, photo):
    original_img_url = 'https://' + str(farm) + '.staticflickr.com/' + str(server_id) + '/' + str(photo)
    text = text.replace('%3F', '?')
    text = text.replace('%23', '#')
    text = text.replace('%5C', '\\')
    response = requests.get(original_img_url)
    selected_image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(selected_image)
    img_width, img_height = selected_image.size
    font_width, font_height = draw.textsize(text)
    font = ImageFont.truetype('arial.ttf', round(float(font_size)))
    draw.text(((img_width - font_width) / 2 - font_width, (img_height - font_height) / 2 - font_height),
              text, font=font, align='center',
              fill=(round(float(font_red)), round(float(font_green)), round(float(font_blue))))
    response = HttpResponse(content_type='image/jpeg')
    selected_image.save(response, 'JPEG')
    return response
