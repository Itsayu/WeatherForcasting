import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = "2112700aec968bedb42e21d314fd9ff7"
# lat = "48.208176"
# lon = "16.373819"
city_list = ["Patna", "Chandigarh", "Delhi", "Mumbai", "London"]
# url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
position = [302, 430, 555, 690, 817]

# response = requests.get(url)
# data = json.loads(response.text)
# print(data)

image = Image.open("post.png")
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('Inter.ttf', size=50)
content = "Latest Weather Forecast"
color = 'rgb(255, 255, 255)'
(x, y) = (55,50)
draw.text((x, y), content, color, font=font)

font = ImageFont.truetype('Inter.ttf', size=35)
# today = date.today()
content = date.today().strftime("%A - %B %d,%Y")
color = 'rgb(255, 255, 255)'
(x, y) = (55,142)
draw.text((x, y), content, color, font=font)

index = 0
for city in city_list:
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    # print(data)

    font = ImageFont.truetype('Inter.ttf', size=52)
    color = 'rgb(0, 0, 0)'
    (x, y) = (135, position[index])
    draw.text((x, y), city, color, font=font)

    font = ImageFont.truetype('Inter.ttf', size=42)
    content = str(data['main']['temp']) + "\u00b0"
    color = 'rgb(255, 255, 255)'
    (x, y) = (600, position[index])
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter.ttf', size=42)
    content = str(data['main']['humidity']) + "%"
    color = 'rgb(255, 255, 255)'
    (x, y) = (810, position[index])
    draw.text((x, y), content, color, font=font)

    index +=1

image.show()

# ------------FOR GET RESULT IN THE FORM OF PNG--------------

image.save("test.png")

# -----------------FOR GET RESULT IN THE FORM OF PDF--------------
image_pdf = image.convert("RGB")
image_pdf.save("test.pdf")