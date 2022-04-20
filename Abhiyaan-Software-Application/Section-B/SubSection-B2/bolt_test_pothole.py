#!/usr/bin/python3

import cv2

pothole_img = cv2.imread('pothole.png') # get the image of the pothole
hsv_pothole = cv2.cvtColor(pothole_img, cv2.COLOR_BGR2HSV) # convert to hsv

pothole_hist = cv2.calcHist([hsv_pothole], [0, 2], None, [20, 256], [0, 20, 0, 256]) # calculate the histogram
cv2.normalize(pothole_hist, pothole_hist, 0, 255, cv2.NORM_MINMAX)# normalize the histogram

capture = cv2.VideoCapture('./bolt_test_pothole.mp4') # create a capture using the video
valid = True

while valid: # loop as long as the frame is valid
    valid, frame = capture.read() # get the current frame
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert the frame to hsv
    Lower = (-10,-40,215)  # lower hsv bound for white rgb = (255.255.255)
    Upper = (10,40,295)  # upper hsv bound for white rgb = (255.255.255)
    binary_image = cv2.inRange(hsv_frame,Lower,Upper)  # generate binary_image_mask
    contours = cv2.findContours(binary_image.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]  # get the contours

    for c in contours:  # for all the contours
        if cv2.contourArea(c) > 200:  # if the area of the contour is significant
            (x, y, w, h) = cv2.boundingRect(c)  # find the coordinates of a bounding rectangle
            cv2.rectangle(frame, (x, y), (x + 2*w, y + 2*h), (255, 0, 0), 2)  # draw the bounding rectangle on frame

    cv2.imshow("Pothole Video", frame)  # display the frame

    if cv2.waitKey(30) == 27:  # wait till the user presses ESC
        break  # break if ESC is pressed

cv2.destroyAllWindows()  # destroy all windows

# References:
# https://stackoverflow.com/questions/51871134/hsv-opencv-colour-range
# https://www.udemy.com/course/ros-essentials/learn/lecture/11347626#overview