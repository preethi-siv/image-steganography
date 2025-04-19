from steganography import hide_message, extract_message

def main():
    print("Image Steganography Tool")
    print("1. Hide a Message")
    print("2. Extract a Message")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        image_path = input("Enter the input file name: ")
        output_image = input("Enter the output file name: ")
        message = input("Enter the secret message to hide: ")
        hide_message(image_path, message, output_image)
        print(f"Message hidden successfully in '{output_image}'.")

    elif choice == '2':
        image_path = input("Enter the input file name: ")
        message = extract_message(image_path)
        print("Extracted Message:", message)

    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
