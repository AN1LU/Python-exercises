import qrcode
# qr_generator.py this module generates a QR code from user input

def generate_qr_code(data, filename='qr_code.png'):
    img = qrcode.make(data)
    save_path = f'./{filename}'
    img.save(save_path)
    print(f"QR code generated and saved as {save_path}")

if __name__ == "__main__":
    try:
        data = input("Enter the data to encode in QR code: ")
        if not data:
            raise ValueError("Data cannot be empty.")
        filename = input("Enter the filename to save QR code (default: qr_code.png): ") or 'qr_code.png'
        generate_qr_code(data, filename)
    except Exception as e:
        print(f"An error occurred: {e}")