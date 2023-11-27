from PIL import Image

with open("A.hex", "wb") as f:
    im = Image.new("L", (64, 64), 128)
    solid = Image.new("L", (im.size[0], im.size[1] // 2), 255)
    im.paste(solid, (0, im.size[1] // 2))
    f.write(im.tobytes())
