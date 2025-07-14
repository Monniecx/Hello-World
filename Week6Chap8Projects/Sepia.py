from PIL import Image

# Load the image
image = Image.open("input.jpg")  # Replace with your image file
pixels = image.load()

# Convert to grayscale first
for y in range(image.height):
    for x in range(image.width):
        r, g, b = pixels[x, y]
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        pixels[x, y] = (gray, gray, gray)

# Apply sepia effect
for y in range(image.height):
    for x in range(image.width):
        r, g, b = pixels[x, y]
        sepia_r = int(min(255, r * 1.2))
        sepia_g = g  # keep green the same
        sepia_b = int(min(255, b * 0.8))
        pixels[x, y] = (sepia_r, sepia_g, sepia_b)

# Save the result
image.save("output_sepia.jpg")
print("Sepia image saved as output_sepia.jpg")
