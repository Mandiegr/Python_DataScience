import cv2
from cvzone.FaceDetectionModule import FaceDetector

video = cv2.VideoCapture(0)

detector = FaceDetector()

num_faces = 0

while True:
    _, img = video.read()
    img, bboxes = detector.findFaces(img, draw=True)  # Desenha caixas de detecção no quadro
    num_faces = len(bboxes)
    
    # Adiciona a contagem de rostos detectados à imagem
    cv2.putText(img, f'Faces: {num_faces}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Exibe a imagem com as detecções
    cv2.imshow('Resultado', img)
    
    # Espera pela tecla 'ESC' ou 'q' para sair
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break

# Libera a captura de vídeo e fecha as janelas
video.release()
cv2.destroyAllWindows()

