from ultralytics import YOLO

# Cargar el modelo YOLO preentrenado
model = YOLO('yolov8n.pt')  # Cambia a yolov8s.pt, yolov8m.pt, etc., si necesitas un modelo diferente

# Entrenar el modelo
model.train(
    data='dataset.yaml',
    epochs=50,
    batch=16,
    imgsz=640,
    name='custom_yolo',
    device='cpu'  # Cambiar a CPU
)
