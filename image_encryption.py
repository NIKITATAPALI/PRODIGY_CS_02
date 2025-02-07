from PIL import Image
import matplotlib.pyplot as plt

def encrypt_or_decrypt_image(input_image_path, output_image_path, key, action):
    image = Image.open(input_image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            pixel = pixels[i, j]
            if len(pixel) == 3:
                r, g, b = pixel
                pixels[i, j] = (r ^ key, g ^ key, b ^ key)
            elif len(pixel) == 4:
                r, g, b, a = pixel
                pixels[i, j] = (r ^ key, g ^ key, b ^ key, a)

    image.save(output_image_path)
    print(f"Image {action}ed and saved to {output_image_path}")

def display_image(image_path, action):
    try:
        image = Image.open(image_path)
        plt.imshow(image)
        plt.title(f"{action.capitalize()} Image")
        plt.axis('off')
        plt.show()
        print(f"{action.capitalize()} image displayed successfully.")
    except FileNotFoundError:
        print(f"Error: The file at path '{image_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while displaying the image: {e}")

def main():
    while True:
        print("\nWelcome to the Image Encryption Tool!")
        print("Choose an option:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Show an encrypted image")
        print("4. Show a decrypted image")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            input_image_path = input("Enter the path to the input image: ").strip()
            output_image_path = input("Enter the path to save the encrypted image: ").strip()
            key = int(input("Enter the encryption key (integer): ").strip())
            encrypt_or_decrypt_image(input_image_path, output_image_path, key, "encrypt")

        elif choice == "2":
            input_image_path = input("Enter the path to the encrypted image: ").strip()
            output_image_path = input("Enter the path to save the decrypted image: ").strip()
            key = int(input("Enter the decryption key (integer): ").strip())
            encrypt_or_decrypt_image(input_image_path, output_image_path, key, "decrypt")

        elif choice == "3":
            image_path = input("Enter the path to the encrypted image: ").strip()
            display_image(image_path, "encrypted")

        elif choice == "4":
            image_path = input("Enter the path to the decrypted image: ").strip()
            display_image(image_path, "decrypted")

        elif choice == "5":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()

