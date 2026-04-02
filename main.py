from PIL import Image

# take input

basepath = input("Input base image path: ").strip('"\'')
overlaypath = input("Input overlay image path: ").strip('"\'')

# create image objects

base = Image.open(basepath).convert("RGBA")
overlay = Image.open(overlaypath).convert("RGBA")

# resize image

overlay_resized = overlay.resize(base.size, Image.Resampling.LANCZOS)

# overlay!

base.paste(overlay_resized, (0, 0), overlay_resized)

# save output

base.save("output.png")
