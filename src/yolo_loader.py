from ultralytics import YOLO

def load_model():
    # Ajusta la ruta según sea necesario
    model_path = "runs/detect/train14/weights/best.pt"
    model = YOLO(model_path)
    return model
