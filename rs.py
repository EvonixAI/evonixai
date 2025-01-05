from PIL import Image

# Load the uploaded favicon image
input_path = "./Evonix AI circle no bg.png"
output_sizes = [16, 32, 48]
output_files = {}

# Resize and save the favicon in different sizes
with Image.open(input_path) as img:
    for size in output_sizes:
        resized_img = img.resize((size, size), Image.ANTIALIAS)
        output_path = f"./fav/f2/favicon_{size}x{size}.png"
        resized_img.save(output_path, format="PNG")
        output_files[f"favicon_{size}x{size}"] = output_path
