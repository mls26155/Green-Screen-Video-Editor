import cv2
import numpy as np

cap = cv2.VideoCapture("Resources/video.mp4")
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("greenscreen1.mp4", fourcc, frame_rate, (w,h))

while True:
    _ , frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv
    lower_green = np.array([60,70,70])
    upper_green = np.array([150,255,255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    try:
        out.write(res)
    except:
        print("Error, not writing to file")
    cv2.imshow("res", res)

    k = cv2.waitKey(2) & 0xFF == ord('q')
    if k == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()