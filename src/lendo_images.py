import pytesseract
import cv2
import matplotlib.pyplot as plt
import numpy as np
import base64

img = cv2.imread("images/cupom-fiscal-1.jpg")
#print(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#cv2.imshow('Cute Kitens', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
plt.figure(figsize=(20,10))
#plt.imshow(img)

extrair = pytesseract.image_to_string(img, lang="por")
print(extrair)

def save_image(image):
    img_bytes = bytearray(image.encode())
    with open("images/recibo.jpg", "wb") as fh:
        fh.write(base64.decodebytes(img_bytes))
        #fh.write(image)

def read_image(id, image):
    save_image(image)
    imagem = cv2.imread("images/recibo.jpg")
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    #imagem_bytes = base64.b64decode(image)
    #im_arr = np.frombuffer(imagem_bytes, dtype=np.uint8)
    #print(im_arr)
    #imagem = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    #imagem = cv2.cvtColor(im_arr, cv2.COLOR_BGR2RGB)
    texto = pytesseract.image_to_string(imagem, lang="por")
    print(texto)
    return texto