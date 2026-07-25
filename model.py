from ultralytics import YOLO

# Load YOLO model only once
MODEL_PATH = "weights/best.pt"

model = YOLO(MODEL_PATH)