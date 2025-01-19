from PIL import Image

def ascii_converter(image_path):
    # Open image and convert to grayscale, and adjust the size of image 
    
    im = Image.open(image_path).convert("L")
    resized_image = im.resize((50, int(50 * im.height / im.width)))
    im = resized_image
    width, height = im.size

    # ASCII characters from lightest to darkest
    ascii_chars = "`.,:;&$%#"
    
    # File to output results
    with open('output.txt', 'w') as f:
    # Iterate through pixels
        for y in range(height):
            line = ""
            for x in range(width):
                pixel = im.getpixel((x, y))
            # Map brightness to ASCII character
                char_index = int(pixel / 256 * len(ascii_chars))
                line += ascii_chars[char_index]
            f.write(line + '\n')

# Example usage
ascii_converter(input())
    
    

