# -*- coding: utf-8 -*-
"""My-QR-Code-Generator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18TZ2wu67fi3ImKCU3n-GlX0f5Ai3ssYU

**A QR code with a more user-friendly interface and experience in a Jupyter notebook by Worachat Wannawong, Ph.D.**

---

To create a QR code with a more user-friendly interface and experience in a Jupyter notebook, you can enhance the code with better input handling and display options. Here's an improved version:
"""

# Install required libraries
!pip install pyqrcode pypng Pillow

import pyqrcode
from PIL import Image
from IPython.display import display, Image as IPImage

# Function to generate and display a QR code
def generate_qr_code():
    # Input prompt with guidance
    s = input("Enter the URL or text for the QR code: ")

    # Create QR code
    url = pyqrcode.create(s)

    # Save the QR code as an image file
    img = "qr-code.png"
    url.png(img, scale=10)

    # Open and display the QR code image
    im = Image.open(img)
    display(im)  # Display the image inline in the notebook
    print("QR code generated and displayed successfully!")

# Run the function
generate_qr_code()

"""Install **pyqrcode** module"""

pip install pyqrcode

"""**Enhancements:**

---

1.  **Guided Input: ** The input prompt provides clear instructions, making it more user-friendly.
2.  **Inline Display: ** The QR code is displayed directly within the notebook using IPython.display, improving the overall user experience.
3.  **Feedback: ** The script confirms successful generation and display of the QR code.

---

This setup should provide a more polished and interactive experience for generating QR codes in Jupyter.


---


**Step by Step: User can start from here**

Install an additional module **pypng** to save image in png format
"""

pip install pypng

"""To open Image, install **Pillow** module"""

pip install Pillow

"""# Code"""

import pyqrcode
import png
from PIL import Image

#inserting website name
s = input("Enter your website: ")
print(s)
url = pyqrcode.create(s)

#saving image
img = "qr-code.png"
url.png(img, scale=10)

#opening image
im=Image.open(img)

#show
im