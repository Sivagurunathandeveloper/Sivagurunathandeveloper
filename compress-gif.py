from PIL import Image
import os

input_file = r"assets\project-carousel .gif"
output_file = r"assets\project-carousel.gif"

im = Image.open(input_file)

frames = []

try:
    while True:
        frame = im.convert("RGB")

        # Reduce dimensions while keeping the carousel clear
        frame.thumbnail((800, 467), Image.Resampling.LANCZOS)

        # Reduce colors to make the GIF much smaller
        frame = frame.quantize(
            colors=96,
            method=Image.Quantize.MEDIANCUT
        )

        frames.append(frame)

        im.seek(im.tell() + 1)

except EOFError:
    pass

print(f"Frames processed: {len(frames)}")

frames[0].save(
    output_file,
    save_all=True,
    append_images=frames[1:],
    duration=170,
    loop=0,
    optimize=True,
    disposal=2
)

size_mb = os.path.getsize(output_file) / (1024 * 1024)

print(f"Created: {output_file}")
print(f"New size: {size_mb:.2f} MB")