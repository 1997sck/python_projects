
# Import QRCode from pyqrcode
import pyqrcode
#import png
from pyqrcode import QRCode

# String which represents the QR code
s = "URL"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("sdc.svg", scale=8)

# Create and save the png file naming "myqr.png"
#"url.png('myqr.png', scale=6)"