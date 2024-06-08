# Fatigue Detection System

This project created for dijital image processing class. this project is a real-time fatigue detection system that uses advanced image processing algorithms to detect eye fatigue. The system leverages the Dlib library for face and eye detection and OpenCV for video capture and display.

## Setup Instructions

Ensure that you have Python 3 installed. You can download it from python.org.

## Navigate to the project directory
```bash
cd Fatigue-Detection-System
```

## Create a virtual environment and activate it
```bash
python3 -m venv fatigue-detection-env
source fatigue-detection-env/bin/activate  # On Windows use `fatigue-detection-env\Scripts\activate`
```

## Install required libraries
```bash
pip install opencv-python dlib numpy scipy requests
```

## Download and extract the model file
```bash
python download_and_extract_model.py
```

## Run the project
```bash
python main.py
```

- Eye Aspect Ratio (EAR) Calculation: The system calculates the eye aspect ratio to determine the openness of the eyes. If the eyes are closed for a certain number of consecutive frames, it indicates fatigue.

- Face and Eye Detection: Using Dlib's pre-trained models, the system detects faces and facial landmarks, which include the coordinates of the eyes.

- Real-time Video Capture: OpenCV captures video from the webcam and processes each frame to detect fatigue.

- Fatigue Alert: If the system detects fatigue, it displays a "FATIGUE DETECTED!" message above the detected face.
