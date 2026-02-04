import cv2 as cv
import numpy as np

cap = cv.VideoCapture("bang_chuyen.mp4")

count = 0
passed = []       # lưu x đã đếm
line_x = 100

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)

    circles = cv.HoughCircles(
        gray,
        cv.HOUGH_GRADIENT,
        dp=1,
        minDist=30,
        param1=100,
        param2=30,
        minRadius=10,
        maxRadius=50
    )

    # vẽ line đếm
    cv.line(frame, (line_x, 0), (line_x, frame.shape[0]), (0, 0, 255), 2)

    if circles is not None:
        circles = np.uint16(np.round(circles))

        for x, y, r in circles[0]:
            cv.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv.circle(frame, (x, y), 2, (0, 0, 255), 3)

            # kiểm tra qua vạch
            if x > line_x and x not in passed:
                passed.append(x)
                count += 1
                print("Count:", count)

    cv.putText(frame, f"Count: {count}", (20, 40),
               cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv.imshow("Frame", frame)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
