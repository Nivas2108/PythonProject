import qrcode
url=input("ENTER URL: ").strip()
file_path="C:\\Users\\Nivas\\OneDrive\\Desktop\\qrcode.png"
qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file_path)
print("QR code is generated")