import qrcode as qr

website = "https://www.github.com/Balaji-R-05"
qr_code = qr.make(website)
qr_code.save("qrcode.png")
