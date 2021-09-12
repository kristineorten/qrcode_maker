# QR-code-maker
This is a simple program that takes in an url and makes a QR-code for it (saved as .png). Note: The code validates the url.

The decoder reveales the text/url behind a QR-code.

## QRcode-maker: Dependencies
You will need the QRcode python module:

`pip install qrcode`

The program also uses a python url validator:

`pip install validators`

## QRcode-decoder: Dependencies
This program requier OpenCV:

`pip install opencv-python`

## Examples of use
### QRcode-maker
`python3 qrcode_maker.py`

```
To exit, type 'exit' og 'quit'
Url of the website you want a QR-code for: https://www.youtube.com/
```

### QRcode-decoder
`python3 qrcode_decoder.py`

```
To exit, type 'exit' og 'quit'
Filename of the QR-code you want to decode: youtubeQR.png
Decoded text is:  https://www.youtube.com/
```
