import cv2
import serial
port = 'COM14'
baud_rate = 9600
# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)
flag = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    bruh = frame.copy()
    bgrey = cv2.cvtColor(bruh, cv2.COLOR_BGR2GRAY)
    # Convert the frame to grayscale (Haar cascades work with grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    #print(len(faces))
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    _ , thresholded = cv2.threshold(bgrey , 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow('Face Detection', frame)
    cv2.imshow('Carti', thresholded)
    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()