import cv2
import captura


# Carrega os classificadores pré-treinados para detecção de rostos, olhos e sorrisos
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')


# Inicializa a captura de vídeo da câmera
capture = cv2.VideoCapture(0)

# Verifica se a câmera está aberta corretamente
if not capture.isOpened():
    print("Não foi possível abrir a câmera")
    exit()

# Loop infinito para captura contínua de frames da câmera
while 1:
    ret, img = capture.read()  #Captura um frame da câmera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converte a imagem para tons de cinza

    # Detecta rostos na imagem em tons de cinza
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces: # Itera sobre cada rosto detectado na imagem
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2) # Itera sobre cada rosto detectado na imagem
        roi_gray = gray[y:y + h, x:x + w]  # Região de interesse em cinza
        roi_color = img[y:y + h, x:x + w] # Região de interesse em cores

        # Detecta olhos na região de interesse do rosto em tons de cinza
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Detecta sorrisos na região de interesse do rosto em tons de cinza
        smile = smile_cascade.detectMultiScale(roi_gray)


        for (ex, ey, ew, eh) in eyes: # Itera sobre cada olho detectado na região de interesse do rosto
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

        for (sx, sy, sw, sh) in smile: # Itera sobre cada sorriso detectado na região de interesse do rosto
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 255), 2)

    cv2.imshow('img', img) # Mostra a imagem com as detecções na janela


    captura.captura_imagem(ret,img) # Chama a função para captura de imagem

    if cv2.waitKey(1) & 0xFF == 27:
        break

# Libera a captura e fecha a janela da câmera
capture.release()
cv2.destroyAllWindows()


