from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open("sample.jpg")
draw = ImageDraw.Draw(img)


text_top = input("Enter some text: ")
s=int(input("Enter size of your text: "))
font = ImageFont.truetype("OpenSans-ExtraBold.ttf", s)

image_width, image_height = img.size


draw.text(
    ((image_width)/ 2, (image_height)/10 ),
    text_top,
    (0,0,0),
    font,
    anchor="mm", 
)



img.save("text_img.jpg")