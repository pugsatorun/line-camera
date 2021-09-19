import cv2
from usbVideoDevice import UsbVideoDevice

usbVideoDevice = UsbVideoDevice()
PORT = 1
cap = cv2.VideoCapture (usbVideoDevice.getId(PORT))

