import pytesseract
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/cupom-fiscal-1.jpg")
print(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#cv2.imshow('Cute Kitens', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
plt.figure(figsize=(20,10))
#plt.imshow(img)

extrair = pytesseract.image_to_string(img, lang="por")
print(extrair)