from PIL import Image, ImageDraw, ImageFont

font = ImageFont.FreeTypeFont("CBDTTestFont.ttf", size=64)

im = Image.new("RGBA", (128, 96), "white")
d = ImageDraw.Draw(im)
d.text((16, 16), "AB", font=font, embedded_color=True)

im.save("AB.png")
im.show()
