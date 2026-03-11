# QR Code Generator (Python)

A simple Python program that generates QR codes from user input (text or URLs) and saves them as PNG images.

The generated QR codes are automatically stored in a `qr_images` folder and opened for preview.

## Features

* Generate QR codes from text or URLs
* Automatically creates a folder for saved images
* Custom filename support
* Opens the generated QR code automatically
* Simple command-line interface

## Tech Stack

* Python
* qrcode library
* Pillow (PIL) for image preview

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

2. Install required libraries

```bash
pip install qrcode[pil]
```

## Usage

Run the script:

```bash
python qr_generator.py
```

Example input:

```
Enter text/URL: https://google.com
Filename [qrcode.png]: myqr
```

Output:

```
QR code saved in: /qr_images/myqr.png
```

The QR code image will also open automatically.

## Project Structure

```
qr-code-generator/
│
├── qr_generator.py
├── qr_images/
└── README.md
```

## How It Works

1. User enters text or URL
2. Program generates a QR code using the qrcode library
3. The image is saved as PNG inside the `qr_images` folder
4. The generated QR code is opened automatically

## Author

Gaurav Dutta
