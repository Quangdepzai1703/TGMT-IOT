import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import time
import math


# img = np.random.randint(0, 256, (768, 1024), dtype=np.uint8) # Tạo ảnh ngẫu nhiên 1024x768 với giá trị pixel từ 0 đến 255
# cv.imshow('Random Image', img)
# key = cv.waitKey(0)
# cv.destroyAllWindows()


# cl_img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)  # Chuyển ảnh xám sang ảnh màu BGR
# cl_img[0:50,0:50,0] = 255
# cl_img[50:90,60:90,1] = 255
# cl_img[150:200,150:200,2] = 255
# cv.imshow('Color Image', cl_img)
# key = cv.waitKey(0)
# cv.destroyAllWindows()


# cimg = np.random.randint(0, 256, (768, 1024, 3), dtype=np.uint8) # Tạo ảnh ngẫu nhiên 1024x768 với 3 kênh màu
# cv.imshow('Rand Color Image', cimg)
# key = cv.waitKey(0)
# cv.destroyAllWindows()

bimg = np.ones((768, 1024,3), dtype=np.uint8) 

bimg[:,:,0] = 50
bimg[:,:,1] = 50
bimg[:,:,2] = 50 #Blue -> Green -> Red 
cv.line(bimg, (1024//2,0), (1024//2, 768), (0,0,255), 1)  #BGR
cv.line(bimg, (0,768//2), (1024, 768//2), (0,0,255), 1)  #BGR
x = 1024//2
y = 768//2
cv.circle(bimg, (x,y), 300, (0,255,0), 2)
cv.circle(bimg, (x,y), 10, (0,255,0), 3)

cv.line(bimg, (x,y), (x+150, y+150), (0,0,255), 5) #gio
cv.line(bimg, (x,y), (x-152, y-152), (255,0,0), 3) #Phut
# cv.line(bimg, (x,y), (x+100, y -100), (0,255,0), 2) #giay

cv.putText(bimg, "XII", (x-45,145), cv.FONT_HERSHEY_COMPLEX, 2, (255,0,255), 4)
cv.putText(bimg, "VI", (x-45,670), cv.FONT_HERSHEY_COMPLEX, 2, (128,128,0), 4)
cv.putText(bimg, "III", (x+250,y+25), cv.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 4)
cv.putText(bimg, "IX", (x-300,y+25), cv.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 4)
# cv.putText(bimg, "IX", (250,350), cv.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 4)


# #color = (123, 125, 128)
# cv.imshow("one image", bimg)
# cv.waitKey(0)

 # Copy ảnh gốc
img = bimg.copy()

# Lấy giây hiện tại
seconds = time.localtime().tm_sec

# Tính góc cho kim giây (0 độ ở 12h, quay theo chiều kim đồng hồ)
second_angle = math.radians((seconds * 6) - 90)

# Tính tọa độ điểm cuối kim giây
second_x = int(x + 152* math.cos(second_angle))
second_y = int(y +  152* math.sin(second_angle))

# Vẽ kim giây
cv.line(img, (x, y), (second_x, second_y), (0, 255, 0), 2)

# Hiển thị
cv.imshow("one image", img)

# Nhấn 'q' để thoát
cv.waitKey(0)


 # Copy ảnh gốc
img = bimg.copy()

# Lấy giây hiện tại
seconds = time.localtime().tm_sec

# Tính góc cho kim giây (0 độ ở 12h, quay theo chiều kim đồng hồ)
second_angle = math.radians((seconds * 6) - 90)

# Tính tọa độ điểm cuối kim giây
second_x = int(x + 152* math.cos(second_angle))
second_y = int(y +  152* math.sin(second_angle))

# Vẽ kim giây
cv.line(img, (x, y), (second_x, second_y), (0, 255, 0), 2)

# Hiển thị
cv.imshow("one image", img)

# Nhấn 'q' để thoát
cv.waitKey(0)

 # Copy ảnh gốc
img = bimg.copy()
# Lấy giây hiện tại
seconds = time.localtime().tm_sec

# Tính góc cho kim giây (0 độ ở 12h, quay theo chiều kim đồng hồ)
second_angle = math.radians((seconds * 6) - 90)

# Tính tọa độ điểm cuối kim giây
second_x = int(x + 152* math.cos(second_angle))
second_y = int(y +  152* math.sin(second_angle))

# Vẽ kim giây
cv.line(img, (x, y), (second_x, second_y), (0, 255, 0), 2)

# Hiển thị
cv.imshow("one image", img)

# Nhấn 'q' để thoát
cv.waitKey(0)

 # Copy ảnh gốc
img = bimg.copy()

# Lấy giây hiện tại
seconds = time.localtime().tm_sec

# Tính góc cho kim giây (0 độ ở 12h, quay theo chiều kim đồng hồ)
second_angle = math.radians((seconds * 6) - 90)

# Tính tọa độ điểm cuối kim giây
second_x = int(x + 152* math.cos(second_angle))
second_y = int(y +  152* math.sin(second_angle))

# Vẽ kim giây
cv.line(img, (x, y), (second_x, second_y), (0, 255, 0), 2)

# Hiển thị
cv.imshow("one image", img)

# Nhấn 'q' để thoát
cv.waitKey(0)

 # Copy ảnh gốc
img = bimg.copy()

# Lấy giây hiện tại
seconds = time.localtime().tm_sec

# Tính góc cho kim giây (0 độ ở 12h, quay theo chiều kim đồng hồ)
second_angle = math.radians((seconds * 6) - 90)

# Tính tọa độ điểm cuối kim giây
second_x = int(x + 152* math.cos(second_angle))
second_y = int(y +  152* math.sin(second_angle))

# Vẽ kim giây
cv.line(img, (x, y), (second_x, second_y), (0, 255, 0), 2)

# Hiển thị
cv.imshow("one image", img)

# Nhấn 'q' để thoát
cv.waitKey(0)

 # Copy ảnh gốc
img = bimg.copy()

# Lấy giây hiện tại
seconds = time.localtime().tm_sec

# Tính góc cho kim giây (0 độ ở 12h, quay theo chiều kim đồng hồ)
second_angle = math.radians((seconds * 6) - 90)

# Tính tọa độ điểm cuối kim giây
second_x = int(x + 152* math.cos(second_angle))
second_y = int(y +  152* math.sin(second_angle))

# Vẽ kim giây
cv.line(img, (x, y), (second_x, second_y), (0, 255, 0), 2)

# Hiển thị
cv.imshow("one image", img)

# Nhấn 'q' để thoát
cv.waitKey(0)

 # Copy ảnh gốc
img = bimg.copy()

# Lấy giây hiện tại
seconds = time.localtime().tm_sec

# Tính góc cho kim giây (0 độ ở 12h, quay theo chiều kim đồng hồ)
second_angle = math.radians((seconds * 6) - 90)

# Tính tọa độ điểm cuối kim giây
second_x = int(x + 152* math.cos(second_angle))
second_y = int(y +  152* math.sin(second_angle))

# Vẽ kim giây
cv.line(img, (x, y), (second_x, second_y), (0, 255, 0), 2)

# Hiển thị
cv.imshow("one image", img)

# Nhấn 'q' để thoát
cv.waitKey(0)

 # Copy ảnh gốc
img = bimg.copy()

# Lấy giây hiện tại
seconds = time.localtime().tm_sec

# Tính góc cho kim giây (0 độ ở 12h, quay theo chiều kim đồng hồ)
second_angle = math.radians((seconds * 6) - 90)

# Tính tọa độ điểm cuối kim giây
second_x = int(x + 152* math.cos(second_angle))
second_y = int(y +  152* math.sin(second_angle))

# Vẽ kim giây
cv.line(img, (x, y), (second_x, second_y), (0, 255, 0), 2)

# Hiển thị
cv.imshow("one image", img)

# Nhấn 'q' để thoát
cv.waitKey(0)

cv.destroyAllWindows()
# plt.imshow(bimg) #Red  --> Green --> Blue
# plt.show()
