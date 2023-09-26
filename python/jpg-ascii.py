from PIL import Image

def convert_image_to_ascii(image_path: str, width: int = 100):
    """
    Converts a JPG image to ASCII art.

    Parameters:
    - image_path: str
        The path to the JPG image file.
    - width: int (default: 100)
        The width of the ASCII art (number of characters per line).

    Returns:
    - str:
        The ASCII art representation of the image.

    Raises:
    - FileNotFoundError:
        If the image file is not found at the specified path.
    """

    # Open the image file
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        raise FileNotFoundError("Image file not found.")

    # Resize the image to match the desired width while maintaining the aspect ratio
    aspect_ratio = image.width / image.height
    height = int(width / aspect_ratio)
    resized_image = image.resize((width, height))

    # Convert the resized image to grayscale
    grayscale_image = resized_image.convert("L")

    # Define the ASCII characters to represent different shades of gray
    ascii_chars = "@%#*+=-:. "

    # Convert each pixel of the grayscale image to an ASCII character
    ascii_art = ""
    for y in range(height):
        for x in range(width):
            pixel_value = grayscale_image.getpixel((x, y))
            ascii_char = ascii_chars[pixel_value // 32]
            ascii_art += ascii_char
        ascii_art += "\n"

    return ascii_art

# Example usage:
image_path = "path/to/image.jpg"
ascii_art = convert_image_to_ascii(image_path)
print(ascii_art)
