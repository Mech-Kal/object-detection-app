import torch
import cv2
import os

class detecting:
    def __init__(self, path, name):
        self.case_name=name
        self.img_path= path

    def detect(self):
        print(self.case_name)
# Load the YOLOv5 model (pre-trained on the COCO dataset)
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load an image
#  # Use forward slashes or double backslashes
        img = cv2.imread(self.img_path)

# Perform inference
        results = model(img)

# Get detected objects
        detections = results.xyxy[0]  # Bounding boxes with format [x1, y1, x2, y2, confidence, class]
        labels = results.names  # Class labels (e.g., 'person', 'car', etc.)

# Create a directory to save the cropped images and results image
        save_dir = f"files/{self.case_name}"

        os.makedirs(save_dir, exist_ok=True)

# Loop through detections and save each object
        for i, det in enumerate(detections):
            x1, y1, x2, y2, conf, cls = map(int, det[:6])  # Bounding box coordinates and class index
            label = labels[cls]  # Get the label name

    # Crop the object from the image
            cropped_img = img[y1:y2, x1:x2]

    # Save the cropped image
            save_path = os.path.join(save_dir, f"{label}_{i}.jpg")
            cv2.imwrite(save_path, cropped_img)

            print(f"Saved {label} to {save_path}")

# Save the full image with bounding boxes and labels manually
# 'results.render()' returns the image with bounding boxes drawn
        rendered_img = results.render()[0]  # Get the image with the detections rendered
        rendered_save_path = os.path.join(save_dir, "image_with_detections.jpg")  # Specify save path
        cv2.imwrite(rendered_save_path, rendered_img)  # Save the rendered image

        print(f"Saved full image with detections to {rendered_save_path}")

# Optionally, display the full image with bounding boxes and labels
        results.show()  # Show the original image with detections


