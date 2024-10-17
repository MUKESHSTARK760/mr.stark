import qrcode
img = qrcode.make("hey bro")
img.save("qrimg.jpg")  




#pip install opencv-python
import cv2
qr_img = cv2.imread("pin.jpg")
qr_det = cv2.QRCodeDetector()
val, pts, st_code = qr_det.detectAndDecode(qr_img)
print("Information:", val)


