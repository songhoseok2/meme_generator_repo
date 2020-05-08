from django.http import HttpResponse
from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO

def display_final_result(self, text, farm, server_id, photo):
    # ... create/load image here ...
    original_img_url = 'https://' + str(farm) + '.staticflickr.com/' + str(server_id) + '/' + str(photo)
    response = requests.get(original_img_url)
    selected_image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(selected_image)
    font = ImageFont.truetype("arial.ttf", 50)
    draw.text((5, 5), text, font=font, align="top")

    # serialize to HTTP response
    response = HttpResponse(content_type="image/jpeg")
    selected_image.save(response, "JPEG")
    return response
