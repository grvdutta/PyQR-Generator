import qrcode
from PIL import Image
import os

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create folder path inside script directory
folder = os.path.join(script_dir, "qr_images")
os.makedirs(folder, exist_ok=True)

# Get user input
text = input("Enter text/URL: ").strip()
filename = input("Filename [qrcode.png]: ").strip() or "qrcode.png"
if not filename.endswith('.png'): filename += '.png'

# Full path
filepath = os.path.join(folder, filename)

# Generate and save QR
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(text)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save(filepath)

print(f"\n✅ QR code saved in: {filepath}")
print(f"📍 Folder: {folder}")

try:
    Image.open(filepath).show()
except:
    print("Open the file manually to view")