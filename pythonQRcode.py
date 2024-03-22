import qrcode
import png

# Tekst atau data yang ingin Anda konversi menjadi QR code
data = "https://www.facebook.com/rdajb"

# Membuat objek QRCode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

# Menambahkan data ke QRCode
qr.add_data(data)
qr.make(fit=True)

# Membuat gambar QRCode
img = qr.make_image(fill_color="black", back_color="white")

# Menyimpan gambar QRCode sebagai file
img.save("qrcode.png")

print("QR code berhasil dibuat.")
