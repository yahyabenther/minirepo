from PIL import Image

# Open the original image
image = Image.open("test.gpj.webp")

# Save the image in a different format (e.g., PNG)
image.save("test.gpj.webp", format="PNG")