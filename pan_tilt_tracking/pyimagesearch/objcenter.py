# import necessary packages
import imutils
import cv2

class ObjCenter:
	def __init__(self, haarPath):
		# load OpenCV's Haar cascade face detector
		self.detector = cv2.CascadeClassifier(haarPath)

	def update(self, frame, frameCenter):
		# convert the frame to grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# detect all faces in the input frame
		rects = self.detector.detectMultiScale(gray, scaleFactor=1.05,
			minNeighbors=9, minSize=(30, 30),
			flags=cv2.CASCADE_SCALE_IMAGE)

		# check to see if a face was found
		if len(rects) > 0:
			# extract the bounding box coordinates of the face and
			# use the coordinates to determine the center of the
			# face
			(x, y, w, h) = rects[0]
			faceX = int(x + (w / 2.0))
			faceY = int(y + (h / 2.0))

			# return the center (x, y)-coordinates of the face
			return ((faceX, faceY), rects[0])

		# otherwise no faces were found, so return the center of the
		# frame
		return (frameCenter, None)