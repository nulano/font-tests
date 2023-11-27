from PIL import Image

size = (64, 64)

glyphs = [("A", "red"), ("B", "blue")]

transparent = Image.new("L", size, 128)
solid = Image.new("L", (size[0], size[1] // 2), 255)
transparent.paste(solid, (0, size[1] // 2))

for glyph, colour in glyphs:
    im = Image.new("RGBA", (64, 64), colour)
    im.putalpha(transparent)
    im.save(f"{glyph}.png")
