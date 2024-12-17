# Import the necessary libraries
import qrcode as qr  # Import the qrcode library for generating QR codes
from PIL import Image  # Import Image from the Pillow library to handle image operations

# Create a QRCode object with specific configurations
qr = qr.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest, up to 40)
    error_correction=qr.ERROR_CORRECT_H,  # Sets the error correction level to High (~30% can be recovered)
    box_size=10,  # Size of each box (module) in pixels
    border=10  # Width of the white border around the QR code (minimum is 4)
)

# Add the data/content that will be encoded into the QR code
qr.add_data("Hello World!!!")  # Replace this with any text, URL, or data you want to encode
qr.make(fit=True)  # Adjusts the size of the QR code to fit the data optimally

# Generate the QR code image with custom colors
img = qr.make_image(
    fill_color="Red",  # Color of the QR code 
    back_color="White"  # Background color of the QR code
)

# Save the generated QR code image to a file
img.save("qrcode.png") 
