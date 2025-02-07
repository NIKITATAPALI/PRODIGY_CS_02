#!/bin/bash

# Function to encrypt/decrypt an image using XOR
encrypt_or_decrypt_image() {
    input_image_path="$1"
    output_image_path="$2"
    key="$3"
    action="$4"

    if [[ ! -f "$input_image_path" ]]; then
        echo "Error: File '$input_image_path' not found!"
        return
    fi

    convert "$input_image_path" -evaluate XOR "$key" "$output_image_path"

    if [[ "$action" == "encrypt" ]]; then
        echo "Image encrypted and saved to $output_image_path"
    else
        echo "Image decrypted and saved to $output_image_path"
    fi
}

# Function to display an image
display_image() {
    image_path="$1"
    action="$2"

    if [[ ! -f "$image_path" ]]; then
        echo "Error: File '$image_path' not found!"
        return
    fi

    display "$image_path" &
    echo "$action image displayed successfully."
}

# Main menu loop
while true; do
    echo -e "\nWelcome to the Image Encryption Tool!"
    echo "Choose an option:"
    echo "1. Encrypt an image"
    echo "2. Decrypt an image"
    echo "3. Show an encrypted image"
    echo "4. Show a decrypted image"
    echo "5. Exit"

    read -p "Enter your choice (1/2/3/4/5): " choice

    case "$choice" in
        1)
            read -p "Enter the path to the input image: " input_image
            read -p "Enter the path to save the encrypted image: " output_image
            read -p "Enter the encryption key (integer): " key
            encrypt_or_decrypt_image "$input_image" "$output_image" "$key" "encrypt"
            ;;
        2)
            read -p "Enter the path to the encrypted image: " input_image
            read -p "Enter the path to save the decrypted image: " output_image
            read -p "Enter the decryption key (integer): " key
            encrypt_or_decrypt_image "$input_image" "$output_image" "$key" "decrypt"
            ;;
        3)
            read -p "Enter the path to the encrypted image: " image_path
            display_image "$image_path" "Encrypted"
            ;;
        4)
            read -p "Enter the path to the decrypted image: " image_path
            display_image "$image_path" "Decrypted"
            ;;
        5)
            echo "Exiting the program. Thank you!"
            exit 0
            ;;
        *)
            echo "Invalid choice! Please enter 1, 2, 3, 4, or 5."
            ;;
    esac
done

