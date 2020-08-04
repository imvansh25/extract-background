import numpy as np
import cv2

file_path = "cut.mp4"

## Function to get background i.e road without vehicles
def static_background(file_path):
	cap = cv2.VideoCapture(file_path)

	first_frame=True
	result = None

	while True:
	    ret, frame = cap.read()
	    if frame is None:
	        break

	    if first_frame:
	        avg = np.float32(frame)
	        first_frame=False
	        
	    cv2.accumulateWeighted(frame, avg, 0.01)
	    result = cv2.convertScaleAbs(avg)

	cv2.imwrite("averaged_frame.jpg", result)
	cv2.waitKey(0)

	cap.release()
	cv2.destroyAllWindows()

static_background(file_path)
