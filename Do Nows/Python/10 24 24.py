import io 
import qrcode

#this code displays the qr straight up 

qr = qrcode.QRCode()
qr.add_data("gus likes drippy cheese")
f = io.stringIO()
qr.print_ascii(out=f)
f = seek(0)
print(f.read())

