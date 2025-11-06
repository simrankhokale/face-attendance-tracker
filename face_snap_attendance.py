import cv2
import csv
from datetime import datetime

# Load OpenCV's built-in Haar Cascade file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)

# CSV file to store attendance
csv_filename = "attendance_log.csv"

# Create CSV file with headers if it doesn’t exist
with open(csv_filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(["Name", "Date", "Time"])

print("📸 Face Attendance System Started — Press 's' to Save Snapshot or 'q' to Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Camera not detected.")
        break

    # Convert frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the video feed
    cv2.imshow("Face Snapshot Attendance", frame)

    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        name = input("Enter name of person: ").strip()
        timestamp = datetime.now()
        date_str = timestamp.strftime("%Y-%m-%d")
        time_str = timestamp.strftime("%H:%M:%S")

        # Save to CSV
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, date_str, time_str])

        # Save snapshot image
        img_name = f"{name}_{timestamp.strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"✅ Snapshot and attendance saved for {name}")

    elif key == ord('q'):
        print("👋 Exiting Face Attendance System...")
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
