# Object Detection App

## Overview
This is a Python-based object detection application that utilizes the YOLOv5 model for detecting objects in images. It provides a GUI using Tkinter for easy image selection and processing.

## Features
- GUI-based image selection and processing using Tkinter
- Object detection using YOLOv5 pre-trained on the COCO dataset
- Cropping and saving detected objects
- Saving the original image with bounding boxes

---

## Tech Stack
- **Python**
- **Tkinter** (GUI for user interaction)
- **OpenCV** (Image processing)
- **PyTorch** (YOLOv5 model inference)

---

## Installation & Setup

### 1. **Clone the Repository**
```sh
git clone https://github.com/Mech-Kal/object-detection-app.git
cd object-detection-app
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```
### 3. Run the Application
```sh
python app.py
```

## Usage
1. Click on "Upload Image" to select an image.
2. Enter a name for the detection case.
3. Click "Detect Objects" to process the image.
4. Detected objects are saved in the files/{case_name} directory.

## Folder Structure
```plaintext
.
├── detect.py        # Object detection script
├── app.py           # Tkinter-based GUI application
├── requirements.txt # Dependencies
├── files/           # Output directory for detected objects
└── README.md        # Project documentation
```

## Future Enhancements
- Add support for video input
- Improve UI/UX with better visual feedback
- Allow users to adjust confidence threshold

## Author
👤 **Kalpak Kamble**

**GitHub:** Mech-Kal

**Email:** kalpak2002@gmail.com