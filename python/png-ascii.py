from PIL import Image

def convert_image_to_ascii(image_path: str, width: int = 100):
    """
    Converts a PNG image to ASCII art.

    Parameters:
    - image_path: str
        The path to the PNG image file.
    - width: int (optional)
        The desired width of the ASCII art. Default is 100.

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

    # Resize the image to the desired width while maintaining aspect ratio
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
            ascii_char = ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]
            ascii_art += ascii_char
        ascii_art += "\n"

    return ascii_art

# Example usage:
image_path = "path/to/image.png"
ascii_art = convert_image_to_ascii(image_path)
print(ascii_art)
