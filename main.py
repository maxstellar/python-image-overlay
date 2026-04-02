from PIL import Image

basepath = input("Input base image path: ")
overlaypath = input("Input overlay image path: ")

base = Image.open(basepath).convert("RGBA")
overlay = Image.open(overlaypath).convert("RGBA")

base.paste(overlay, (0, 0), overlay)

base.save("output.png")