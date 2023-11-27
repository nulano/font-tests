from PIL import Image, ImageDraw, ImageFont

font = ImageFont.FreeTypeFont("EBDTTestFont.ttf", size=64)

modes = [("L", False), ("RGBA", True)]

for mode, embedded_color in modes:
    im = Image.new("RGBA", (128, 96), "white")
    d = ImageDraw.Draw(im)
    d.text((16, 16), "AA", font=font, embedded_color=embedded_color, fill="black")

    im.save(f"AA_{mode}.png")
    im.show()
