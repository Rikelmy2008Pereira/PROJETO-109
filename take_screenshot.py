import numpy as np
import cv2
import pyautogui
import imutils

screenshot = pyautogui.screenshot()

image_np = np.array(screenshot)
image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

cv2.imwrite('screenshot.png', image_np)

loaded_image = cv2.imread('screenshot.png')

cv2.imshow('Screenshot', loaded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
