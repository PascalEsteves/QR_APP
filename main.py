import qrcode
from PIL import Image

def generate_qr_code(data, file_name, size=(256, 256)):
    """
    Generate a QR code image
    :param data: Data to be encoded in the QR code
    :param file_name: File name of the QR code image
    :param size: Size of the QR code image (default is 256x256)
    """
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code instance
    qr.add_data(data)
    qr.make(fit=True)
    print(qr.data)
    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white", size=size)

    # Save the image to a file
    img.save(file_name)

# Example usage
generate_qr_code("virok", "virok.png")