from ultralytics import YOLO
import os

model = YOLO('yolov8n.pt')  # 使用官方预训练模型

def analyze_object(img_path):
    result = model.predict(img_path, save=True, save_txt=False)
    img_output_path = os.path.join("runs", "detect", "predict", os.path.basename(img_path))
    return img_output_path