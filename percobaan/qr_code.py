import segno 
qrcode = segno.make_qr("https://www.instagram.com/fndz1_?igsh=MWZ1aHdpZ3Q5c2gwag==")
qrcode.save(
    "tes_qr.png",
    scale = 5,
)
