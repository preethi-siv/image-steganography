from PIL import Image

def message_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message)

def binary_to_message(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def hide_message(image_path, secret_message, output_image):
    image = Image.open(image_path)
    encoded = image.copy()

    binary_message = message_to_binary(secret_message) + '1111111111111110'  # end marker
    binary_index = 0

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if binary_index >= len(binary_message):
                break

            r, g, b = image.getpixel((x, y))

            if binary_index < len(binary_message):
                r = (r & ~1) | int(binary_message[binary_index])
                binary_index += 1
            if binary_index < len(binary_message):
                g = (g & ~1) | int(binary_message[binary_index])
                binary_index += 1
            if binary_index < len(binary_message):
                b = (b & ~1) | int(binary_message[binary_index])
                binary_index += 1
            encoded.putpixel((x, y), (r, g, b))

        if binary_index >= len(binary_message):
            break

    encoded.save(output_image)

def extract_message(image_path):
    image = Image.open(image_path)
    binary_data = ""

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            r, g, b = image.getpixel((x, y))
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    end_marker = '1111111111111110'
    end_index = binary_data.find(end_marker)
    if end_index != -1:
        binary_data = binary_data[:end_index]

    return binary_to_message(binary_data)