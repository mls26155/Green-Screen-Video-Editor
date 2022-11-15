import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4");

scale = 0.5;
_, frame = cap.read();
h,w = frame.shape[:2];
h = int(h*scale);
w = int(w*scale);

res = (w, h);
fourcc = cv2.VideoWriter_fourcc(*'XVID');
out = cv2.VideoWriter('test_vid.avi',fourcc, 30.0, res);

done = False;
while not done:
    # get frame
    ret, img = cap.read();
    if not ret:
        done = True;
        continue;

    img = cv2.resize(img, res);

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
    h,s,v = cv2.split(hsv);

    unique_colors, counts = np.unique(s, return_counts=True);

    big_color = None;
    biggest = -1;
    for a in range(len(unique_colors)):
        if counts[a] > biggest:
            biggest = counts[a];
            big_color = int(unique_colors[a]);

    margin = 50;
    mask = cv2.inRange(s, big_color - margin, big_color + margin);

    kernel = np.ones((3,3), np.uint8);
    mask = cv2.dilate(mask, kernel, iterations = 1);
    mask = cv2.medianBlur(mask, 5);
    mask = cv2.bitwise_not(mask);
    crop = np.zeros_like(img);
    crop[mask == 255] = img[mask == 255];
    cv2.imshow("Mask", mask);
    cv2.imshow("Blank", crop);
    cv2.imshow("Image", img);
    done = cv2.waitKey(1) == ord('q');
    out.write(crop);

cap.release();
out.release();
