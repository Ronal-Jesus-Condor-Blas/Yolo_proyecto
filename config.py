import os

CONFIG = {
    "YOLO_MODEL_PATH": "models/yolov8n.pt",
    "VIDEO_INPUT_PATH": "data/videos/",
    "RESULTS_PATH": "data/results/",
    "LIVE_STREAM_URL": "rtsp://usuario:contraseña@ip:puerto",  # Cambia esto para el análisis en vivo
}

# Generar lista de videos automáticamente
CONFIG["VIDEOS"] = [f for f in os.listdir(CONFIG["VIDEO_INPUT_PATH"]) if f.endswith(('.mp4', '.avi'))]
