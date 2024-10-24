import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)

qr.add_data("gus likes drippy cheese")
qr.make(fit=True)

img = qr.make_image(fill='black', black_color='white')

img.save("qr_code_output.jpg")