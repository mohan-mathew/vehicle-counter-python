import cv2
import numpy as np
from time import sleep

min_width=80 #min width
min_height=80 #min height

offset=6

Pos_of_line=600 #Position of the count line

delay= 60 #FPS vídeo

detec = []
vehicles= 0


def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

cap = cv2.VideoCapture('video.mp4')

subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret , frame1 = cap.read()
    time = float(1/delay)
    sleep(time)
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))  #to make something larger
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
    dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    conto,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, Pos_of_line), (1200, Pos_of_line), (255,127,0), 3)
    for(i,c) in enumerate(conto):
        (x,y,w,h) = cv2.boundingRect(c)
        validar_contorno = (w >= min_width) and (h >= min_height)     #validate_outline

        if not validar_contorno:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        centers = center(x, y, w, h)
        detec.append(centers)
        cv2.circle(frame1, centers, 4, (0, 0,255), -1)

        for (x,y) in detec:
            if y<(Pos_of_line+offset) and y>(Pos_of_line-offset):
                vehicles+=1
                cv2.line(frame1, (25, Pos_of_line), (1200, Pos_of_line), (0,127,255), 3)  
                detec.remove((x,y))
                print("car is detected : "+str(vehicles))
       
    cv2.putText(frame1, "VEHICLE COUNT : "+str(vehicles), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
    cv2.imshow("Video Original" , frame1)
    cv2.imshow("Detectar",dilatada)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
