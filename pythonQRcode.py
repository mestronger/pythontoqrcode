import qrcode

img = qrcode.make('https://wa.me/6281378893790')
img.save('myQRcod.png')
img.show()
