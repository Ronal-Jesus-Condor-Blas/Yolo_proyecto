import cv2
import os

def extract_frames(video_path, output_folder, frame_interval=30):
    """
    Extrae fotogramas de un video y los guarda como imágenes.
    :param video_path: Ruta al video.
    :param output_folder: Carpeta donde se guardarán los fotogramas.
    :param frame_interval: Intervalo de fotogramas a extraer.
    """
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            output_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(output_path, frame)

        frame_count += 1

    cap.release()
    print(f"Fotogramas extraídos y guardados en {output_folder}")

if __name__ == "__main__":
    video_path = "data/videos/1737160430143.mp4"  # Cambia por el video deseado
    output_folder = "data/images/"
    extract_frames(video_path, output_folder)
