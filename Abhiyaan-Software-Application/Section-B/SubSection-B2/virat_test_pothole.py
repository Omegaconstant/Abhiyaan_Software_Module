#!/usr/bin/python3

import cv2

barrel_img = cv2.imread('barrel.png')  # get the image of the barrel
hsv_barrel = cv2.cvtColor(barrel_img, cv2.COLOR_BGR2HSV)  # convert to hsv

barrel_hist = cv2.calcHist([hsv_barrel], [0, 2], None, [20, 256], [0, 20, 0, 256])  # calculate the histogram
cv2.normalize(barrel_hist, barrel_hist, 0, 255, cv2.NORM_MINMAX)  # normalize the histogram

capture = cv2.VideoCapture('./virat_test_pothole.mp4')  # create a capture using the video

valid = True
while valid:  # loop as long as the frame is valid
    valid, frame = capture.read()  # get the current frame
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # convert the frame to hsv
    Lower = (0,164,0)  # upper hsv bound for orange
    Upper = (179,255,255)  # upper hsv bound for orange
    binary_image = cv2.inRange(hsv_frame,Lower,Upper)  # generate binary_image_mask
    contours = cv2.findContours(binary_image.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]  # get the contours

    for c in contours:  # for all the contours
        if cv2.contourArea(c) > 200:  # if the area of the contour is significant
            (x, y, w, h) = cv2.boundingRect(c)  # find the coordinates of a bounding rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # draw the bounding rectangle on frame

    cv2.imshow("Barrel Video", frame)  # display the frame

    if cv2.waitKey(30) == 27:  # wait till the user presses ESC
        break  # break if ESC is pressed

cv2.destroyAllWindows()  # destroy all windows
capture.release()  # release the capture object

# References:
# https://stackoverflow.com/questions/51871134/hsv-opencv-colour-range
# https://www.udemy.com/course/ros-essentials/learn/lecture/11347626#overview