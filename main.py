from PIL import Image

basepath = input("Input base image path: ").strip('"\'')
overlaypath = input("Input overlay image path: ").strip('"\'')

base = Image.open(basepath).convert("RGBA")
overlay = Image.open(overlaypath).convert("RGBA")

overlay_resized = overlay.resize(base.size, Image.Resampling.LANCZOS)

base.paste(overlay_resized, (0, 0), overlay_resized)

base.save("output.png")
