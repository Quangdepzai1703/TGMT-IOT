import cv2 as cv
import numpy as np
import time

if __name__=="__main__":
    # khởi tạo đọc từ webcam
    cap = cv.VideoCapture(0) 
    base_frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame is not None:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            gray = cv.GaussianBlur(gray, (25, 25), 0)
        if base_frame is None:
            base_frame = gray
            continue

        # tim su khac biet giua 2 khung hinh
        delta = cv.absdiff(base_frame, gray)
        _, nguong = cv.threshold(delta, 25, 255, cv.THRESH_BINARY)
        # giản nở biên
        nguong = cv.dilate(nguong, None, iterations=2)
        # tìm đường biên bao phủ vùng chuyển động
        bien, _ = cv.findContours(nguong.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        for b in bien:
            if cv.contourArea(b) < 100:
                continue
            (x, y, w, h) = cv. boundingRect(b)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0 ), 2)
        cv.imshow("frame", frame)
        cv.imshow("Bw", nguong )
        if cv.waitKey(1) == ord('q'):
                break
    cv.destroyAllWindows()