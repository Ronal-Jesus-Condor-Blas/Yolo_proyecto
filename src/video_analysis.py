import cv2
from src.yolo_loader import load_model
from src.utilities import calculate_times, save_results
from config import CONFIG

def analyze_video(video_name):
    """
    Analiza un video y calcula el tiempo de puerta abierta/cerrada.
    """
    # Cargar el modelo YOLOv8
    model = load_model()

    # Ruta al video
    video_path = f"{CONFIG['VIDEO_INPUT_PATH']}{video_name}"
    cap = cv2.VideoCapture(video_path)
    detections = []

    # Umbral de confianza ajustado
    confidence_threshold = 0.0,5  # Ajusta este valor según sea necesario

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Realizar detección con YOLOv8
        results = model(frame)

        # Depuración: Imprime las predicciones
        print(results[0].boxes)

        if len(results[0].boxes) > 0:
            for box in results[0].boxes:
                class_id = int(box.cls[0])
                confidence = box.conf[0]
                print(f"Detección: Clase {class_id}, Confianza {confidence}")  # Depuración

                # Determinar estado según la clase y confianza
                if class_id == 0 and confidence > confidence_threshold:
                    state = "cerrada"
                elif class_id == 1 and confidence > confidence_threshold:
                    state = "abierta"
                else:
                    continue  # Ignorar detecciones con baja confianza

                # Añadir detección a la lista con timestamp
                detections.append({
                    "state": state,
                    "timestamp": cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Tiempo en segundos
                })

        # Visualizar resultados anotados
        annotated_frame = results[0].plot()
        cv2.imshow("Detección de Puerta", annotated_frame)

        # Salir si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Calcular tiempos y guardar resultados
    results = calculate_times(detections)
    save_results(results, f"{CONFIG['RESULTS_PATH']}{video_name}_results.txt")
    print("Resultados guardados correctamente.")
