import qrcode as qr
i = input("Enter the content for which you need a qr code:")
img = qr.make(i)
img.save("qr.png")