import cv2 as cv
import mediapipe as mp 

video = cv.VideoCapture(0)

while True:
	is_true, frame = video.read()

	cv.imshow('frame', frame)

	if cv.WaitKey(1) & 0xFF == ord('q'):
		break 


cv.release()
cv.DestroyAllWindows()