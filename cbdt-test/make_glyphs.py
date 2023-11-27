from PIL import Image

glyphs = [("A", "red"), ("B", "blue")]

for glyph, colour in glyphs:
    im = Image.new("RGBA", (64, 64), colour)

    transparent = Image.new("L", im.size, 128)
    solid = Image.new("L", (im.size[0], im.size[1] // 2), 255)
    transparent.paste(solid, (0, im.size[1] // 2))
    im.putalpha(transparent)

    im.save(f"{glyph}.png")
