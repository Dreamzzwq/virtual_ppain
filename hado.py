import cv2

cam = cv2.VideoCapture(1)

cv2.namedWindow("window")

img_counter = 1

while True:
    ret, frame = cam.read()
    if not ret:
        print("Laptop Mu ato programmu kentang icibos")
        break
    cv2.imshow("window", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # esc for keluar/destroy window
        print("Sabarr")
        break
    elif k % 256 == 32:
        # space for ss
        img_name = "ss_dulu_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} cekrek!".format(img_name))
        img_counter += 3

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()