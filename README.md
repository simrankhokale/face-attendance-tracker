# face-attendance-tracker
# 🎯 Face Snapshot Attendance System  
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A simple and effective **Face Detection–Based Attendance System** that uses **OpenCV** to capture face snapshots and record attendance in real time.  
This project can be integrated into classrooms, offices, or internship portfolios to demonstrate computer vision skills.

---

## 🧠 Features
- Real-time face detection using **OpenCV Haar Cascade**  
- Automatically captures snapshots with timestamps  
- Attendance is logged in a **CSV file** (`attendance_log.csv`)  
- Works smoothly on **any webcam**  
- Lightweight and beginner-friendly  

---

## 🛠️ Technologies Used
- **Python 3.11+**  
- **OpenCV** – for face detection  
- **CSV & Datetime** – for logging attendance  
- **OS Library** – for file management  

---

## 📸 Project Preview
| Face Detection | Attendance Log |
|----------------|----------------|
| ![Face Detection](https://github.com/user-attachments/assets/example_face_detection.gif) | ![Attendance Log](https://github.com/user-attachments/assets/example_csv_preview.png) |

> *(You can replace these images after uploading your demo GIF or screenshots to GitHub.)*

---

## 📂 Files Generated
| File | Description |
|------|-------------|
| `face_snap_attendance.py` | Main Python file |
| `attendance_log.csv` | Stores attendance (Name, Date, Time) |
| `snapshots/` | Folder that saves face snapshots |

---

## ▶️ How to Run
1. **Install dependencies:**
   ```bash
   pip install opencv-python
