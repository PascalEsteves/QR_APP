import qrcode
from PIL import Image
import cv2
from pyzbar.pyzbar import decode
import os

def scan_qr_code(image_array: str)->str:
    """
    Reads QR code images
    Args: 
        :params image_array array with image values
    Returns: Image decoded
    """
    image_array = bytearray(image_array)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    codes = decode(image)

    return codes.data.decode('utf-8')

def generate_qr_code(data, file_name, size=(256, 256)) -> str:

    """
    Generate a QR code image
    Args:
        :param data: Data to be encoded in the QR code
        :param file_name : File name of the QR code image
        :param size : size of the QR code image (default is 256x256)
    Returns:
        :param qr_location : Location of QR code image
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black", 
        back_color="white", 
        size=size
    )
    if not os.path.exists("Data/QR_IMAGES"):
        os.makedirs("Data/QR_IMAGES")

    filepath = os.path.join("Data",'QR_IMAGES',file_name)
    img.save(filepath)

    return filepath