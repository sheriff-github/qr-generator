import qrcode

img = qrcode.make('https://youtube.com/shorts/zie0FY75d8c?feature=share')
  
img.save("myqr.png")
