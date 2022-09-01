
import qrcode

qr_matn = input('matn ra vared konid : ')

qr_address = input('address ra vared konid : ')

Qr =qrcode.make(qr_matn)
Qr.save(qr_address)
