from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_image(input_path, output_path, key):
    with open(input_path, "rb") as input_file:
        plaintext = input_file.read()

    cipher = AES.new(key, AES.MODE_CBC)  # Use CBC mode for better security
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_path, "wb") as output_file:
        output_file.write(cipher.iv + ciphertext)  # Store IV along with ciphertext

def decrypt_image(encrypted_output_path, decrypted_output_path, key):
    with open(encrypted_output_path, "rb") as encrypted_output_file:
        data = encrypted_output_file.read()
        iv, ciphertext = data[:AES.block_size], data[AES.block_size:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(decrypted_output_path, "wb") as decrypted_output_file:
        decrypted_output_file.write(decrypted_data)

def main():
    key = b'Sixteen byte key'
    input_path = r"C:\Users\siddi\OneDrive\Documents\Downloads\dnld\sampleimg.jpg"
    encrypted_output_path = r"C:\Users\siddi\OneDrive\Documents\Downloads\dnld\encrypted_image.jpg"
    decrypted_output_path = r"C:\Users\siddi\OneDrive\Documents\Downloads\dnld\decrypted_image.jpg"

    try:
        encrypt_image(input_path, encrypted_output_path, key)
        decrypt_image(encrypted_output_path, decrypted_output_path, key)
        print("Image encrypted and saved successfully.")
        print("Image decrypted and saved successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()