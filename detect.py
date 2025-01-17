from ultralytics import YOLO
import cv2

# Cargar el modelo YOLOv8
model = YOLO('yolov8n.pt')

# Ejecutar detección en una imagen
results = model('zidane.jpg', show=True)

# Mantener la ventana abierta hasta que presiones una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
