from ultralytics import YOLO
from config import CONFIG

def load_model():
    """
    Carga el modelo YOLOv8 desde la ruta especificada en la configuración.
    """
    return YOLO(CONFIG["YOLO_MODEL_PATH"])
