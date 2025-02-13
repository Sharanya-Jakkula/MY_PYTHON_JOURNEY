import qrcode as qr
img=qr.make("https://www.youtube.com/")# youtube link
img.save("Youtube_qrcode.png")
