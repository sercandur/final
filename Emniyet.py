import cv2
import mediapipe as mp
import time
from datetime import datetime

now = datetime.now()

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
# cv2.namedWindow("corax",cv2.WND_PROP_FULLSCREEN)
pTime = 0
cTime = 0
wCam, hCam = 1024, 768


def plcYaz():
    print("El var")


cx = 0
cy = 0
elvar = "0"
hiz = 0
calismadurum = "None"
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB,0)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks != None:
        # global elvar
        elvar = "EL VAR"
        cv2.putText(img, str(elvar) + str(" ") + str(cx) + str(" ") + str(cy), (1, 30), cv2.FONT_ITALIC, 0.7,
                    (0, 0, 255), 2)
        hiz = '%10'
        cv2.putText(img, str("SARIM MOTORU HIZI: ") + str(hiz), (1, 80), cv2.FONT_ITALIC, 0.7, (0, 0, 255), 2)
        calismadurum = "Yavaslatildi....."
        cv2.putText(img, str("Makina Durumu: ") + str(calismadurum), (1, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 0, 255), 2)

    else:
        cv2.putText(img, str("El yok") + str(" ") + str(cx) + str(" ") + str(cy), (1, 30), cv2.FONT_ITALIC, 0.7,
                    (70, 255, 0), 2)
        hiz = '%100'
        cv2.putText(img, str("SARIM MOTORU HIZI: ") + str(hiz), (1, 80), cv2.FONT_ITALIC, 0.7, (0, 255, 0), 2)
        calismadurum = "Normal calisma....."
        cv2.putText(img, str("Makina Durumu: ") + str(calismadurum), (1, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 255, 0), 2)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                # if id == 4:
                cv2.circle(img, (cx, cy), 2, (0, 255, 0), 8)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    # "current_time = "now.strftime("%H:%M:%S")
    cv2.putText(img, str(time.strftime("%Y:%m:%d  %H:%M:%S")), (1, 180), cv2.FONT_ITALIC, 0.7, (255, 0, 0), 2)
    # cv2.rectangle(img,(100,100),1,(0,0,255))
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.imshow("El algilama emniyet sistemi", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break