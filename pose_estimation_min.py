import cv2 as cv
import mediapipe as mp 
import time

video = cv.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpdraw = mp.solutions.drawing_utils

ptime = 0

while True:
	is_true, frame = video.read()

	image_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	results = pose.process(image_rgb)
	# print(results.pose_landmarks)

	if results.pose_landmarks == True:
		mpdraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
		for id, lm in enumerate(result.pose_landmarks.landmark):
			h, w, c = frame.shape 
			print(id, lm)
			cx, cy = int(lm.x*w), int(lm.y*h)
			cv.circle(frame, (cx,cy), 10, (255,0,0), cv.FILLED)

	ctime  = time.time()
	fps = 1/(ctime-ptime)
	ptime = ctime

	cv.putText(frame, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
	cv.imshow('frame', frame)

	if cv.waitKey(1) & 0xFF == ord('q'):
		break 


video.release()
cv.destroyAllWindows()