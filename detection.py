import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist

def calculate_ear(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("dataset/shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 48
COUNTER = 0

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    
    for face in faces:
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (102, 0, 153), 3)
        
        landmarks = predictor(gray, face)
        
        left_eye = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)])
        
        right_eye = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)])
        
        for eye in left_eye:
            cv2.circle(frame, eye, 2, (0, 255, 0), -1)
            
        for eye in right_eye:
            cv2.circle(frame, eye, 2, (0, 255, 0), -1)
        
        leftEAR = calculate_ear(left_eye)
        rightEAR = calculate_ear(right_eye)
        
        ear = (leftEAR + rightEAR) / 2.0
        
        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                cv2.putText(frame, "YORGUNLUK ALGILANDI!", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
        else:
            COUNTER = 0
        
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()