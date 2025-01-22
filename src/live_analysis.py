import time
import cv2
from src.yolo_loader import load_model
from src.utilities import calculate_times
from config import CONFIG

def analyze_live():
    """
    Análisis en tiempo real desde una cámara en vivo.
    """
    stream_url = CONFIG["LIVE_STREAM_URL"]
    model = load_model()
    cap = cv2.VideoCapture(stream_url)
    if not cap.isOpened():
        print("Error: No se pudo conectar a la cámara en vivo.")
        return

    detections = []
    print("Iniciando análisis en vivo...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame. Finalizando...")
            break

        results = model(frame)
        if len(results[0].boxes) > 0:
            for box in results[0].boxes:
                class_id = int(box.cls[0])
                confidence = box.conf[0]
                if class_id == 0 and confidence > 0.5:
                    state = "abierta"
                else:
                    state = "cerrada"
                detections.append({"state": state, "timestamp": time.time()})

        annotated_frame = results[0].plot()
        cv2.imshow("Detección en Vivo", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Finalizando detección en vivo...")
            break

    cap.release()
    cv2.destroyAllWindows()

    results = calculate_times(detections)
    print("Resultados finales:", results)
