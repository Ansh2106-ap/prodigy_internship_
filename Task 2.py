from PIL import Image
import os

def encrypt_decrypt_image(input_image_path, output_image_path, key):
    # Check if file exists
    if not os.path.isfile(input_image_path):
        print("❌ Input image not found.")
        return

    # Validate key
    try:
        key = int(key)
        if key < 0 or key > 255:
            raise ValueError
    except:
        print("❌ Key must be an integer between 0 and 255.")
        return

    try:
        img = Image.open(input_image_path)

        # Convert image to RGB or RGBA
        if img.mode == "RGBA":
            pixels = img.load()
            width, height = img.size

            for x in range(width):
                for y in range(height):
                    r, g, b, a = pixels[x, y]
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key, a ^ key)

        else:
            img = img.convert("RGB")
            pixels = img.load()
            width, height = img.size

            for x in range(width):
                for y in range(height):
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        # Create output folder if needed
        out_dir = os.path.dirname(output_image_path)
        if out_dir != "" and not os.path.exists(out_dir):
            os.makedirs(out_dir)

        img.save(output_image_path)
        print("✅ Image processed successfully!")

    except Exception as e:
        print("❌ Error:", e)

# ---------------- MAIN ----------------
def main():
    print("\n🔐 Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Enter choice (1 or 2): ")

    if choice not in ["1", "2"]:
        print("❌ Invalid choice")
        return

    input_image = input("Enter input image path: ")
    output_image = input("Enter output image path: ")
    key = input("Enter key (0-255): ")

    encrypt_decrypt_image(input_image, output_image, key)

    if choice == "1":
        print("🔒 Image Encrypted!")
    else:
        print("🔓 Image Decrypted!")

if __name__ == "__main__":
    main()
    