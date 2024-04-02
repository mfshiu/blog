from PIL import Image, ImageDraw

# Load the image
icon_path = "素材/favicon.webp"
icon_img = Image.open(icon_path)

# Calculate the size for a square based on the smaller side of the image
size = min(icon_img.size)

# Find bounding box coordinates
# left = (icon_img.width - size)/2
# top = (icon_img.height - size)/2
# right = (icon_img.width + size)/2
# bottom = (icon_img.height + size)/2
padding_size = 150
left = padding_size
top = padding_size
right = icon_img.width - padding_size
bottom = icon_img.height - padding_size

# Crop to a square
icon_img = icon_img.crop((left, top, right, bottom))

# Create a new image with white background and same size
circle_img = Image.new('RGBA', icon_img.size, (255, 255, 255, 0))

# Create a mask to make the circular shape
mask = Image.new('L', icon_img.size, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + icon_img.size, fill=255)

# Paste the icon on the white background using the mask
circle_img.paste(icon_img, (0, 0), mask)

# Save the result
circle_icon_path = "素材/circle_icon.png"
circle_img.save(circle_icon_path)

circle_icon_path
