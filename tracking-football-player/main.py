import cv2
import os

#rastreador = cv2.TrackerKCF_create() # Algoritmo KCF

rastreador = cv2.TrackerCSRT_create() # Algorítimo CSRT

video_path = r'C:\Senac\I.A\visao-computacional\tracking-football-player\video_football.mp4'

video = cv2.VideoCapture(video_path)

ok, frame = video.read() # Leitura do primeiro frame do vídeo. A variável ok retornará True se for feita a leitura e False se der erro.

bbox = cv2.selectROI(frame) # Selecionando o bounding box, passando o primeiro frame do vídeo.
#print(bbox) aqui você verá a posição de x, y, w, h do bounding box

ok = rastreador.init(frame, bbox) # Iniciando o rastreamento, passando o frame inicial e a posição do objeto.
 

while True: # para percorrer todo o vídewo.
    ok, frame = video.read()
    
    if not ok: # Se a variável ok for igual a falso, o programa para de executar.
        break

    ok, bbox = rastreador.update(frame) # Atualizando os frames.
   
    if ok: # Criando o bounding box
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1) # Desenhando o retângulo.
    else:
        cv2.putText(frame, 'Erro', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255)) # Configurando mensagem de erro.
    
    cv2.imshow('Rastreamento', frame)

    if cv2.waitKey(1) & 0XFF == 27: # Incluindo a tecla ESC para interromper a execução.
        break


video.release() # Liberando recursos
cv2.destroyAllWindows()



